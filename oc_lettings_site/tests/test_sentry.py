"""Test pour sentry_config.py et audit_decorator.py."""

import sys
import logging
import pytest

import oc_lettings_site.sentry_config as sc
import oc_lettings_site.utils.audit_decorator as ad


def test_before_send_masks_email():
    """Vérifie que les emails sont masqués dans les messages envoyés à Sentry."""
    event = {"message": "Contact me at test@example.com"}
    result = sc._before_send(event, None)
    assert " [at] " in result["message"]
    assert "@" not in result["message"]


def test_get_audit_logger_singleton():
    """Vérifie que get_audit_logger renvoie toujours le même logger."""
    logger1 = sc.get_audit_logger()
    logger2 = sc.get_audit_logger()
    assert logger1 is logger2
    # Vérifie qu'il a bien un handler console
    assert any(isinstance(h, logging.StreamHandler) for h in logger1.handlers)


def test_init_sentry_without_dsn(monkeypatch, caplog):
    """Vérifie que init_sentry loggue un warning si SENTRY_DSN absent."""
    monkeypatch.delenv("SENTRY_DSN", raising=False)
    caplog.set_level(logging.WARNING)
    sc._sentry_initialized = False  # reset état global
    sc.init_sentry()
    assert "Sentry désactivé" in caplog.text


def test_init_sentry_with_dsn(monkeypatch):
    """Vérifie que init_sentry initialise sentry_sdk avec les bons paramètres."""
    monkeypatch.setenv("SENTRY_DSN", "http://fake-dsn")
    monkeypatch.setenv("SENTRY_ENV", "ci")
    monkeypatch.setenv("SENTRY_RELEASE", "test@1.0.0")
    sc._sentry_initialized = False  # reset état global
    # Monkeypatch sentry_sdk.init pour ne pas faire de vrai call
    called = {}

    def fake_init(**kwargs):
        called.update(kwargs)

    monkeypatch.setattr(sc.sentry_sdk, "init", fake_init)
    sc.init_sentry()
    assert called["dsn"] == "http://fake-dsn"
    assert called["environment"] == "ci"


def test_install_global_exception_hook(monkeypatch, caplog):
    """Vérifie que l'exception hook loggue une erreur non gérée."""
    caplog.set_level(logging.CRITICAL)
    sc._hook_installed = False  # reset
    # Monkeypatch capture_exception pour éviter un vrai envoi
    monkeypatch.setattr(sc, "capture_exception", lambda e: None)
    sc.install_global_exception_hook()
    # Provoque une exception via sys.excepthook
    exc_type, exc, tb = ValueError, ValueError("boom"), None
    sys.excepthook(exc_type, exc, tb)
    assert "Unhandled exception" in caplog.text


def test_audit_breadcrumb(monkeypatch):
    """Vérifie que audit_breadcrumb appelle sentry_sdk.add_breadcrumb avec les bons paramètres."""
    called = {}

    def fake_add_breadcrumb(**kwargs):
        called.update(kwargs)

    monkeypatch.setattr(sc, "add_breadcrumb", fake_add_breadcrumb)
    sc.audit_breadcrumb("cat", "msg", {"x": 1})
    assert called["category"] == "cat"
    assert called["message"] == "msg"
    assert called["data"] == {"x": 1}


def test_audit_event(monkeypatch):
    """Vérifie que audit_event appelle sentry_sdk.capture_message avec les bons paramètres."""
    called = {}
    monkeypatch.setattr(
        sc,
        "capture_message",
        lambda m, level=None: called.update({"m": m, "level": level}),
    )
    monkeypatch.setattr(sc.sentry_sdk, "set_context", lambda *a, **kw: None)
    sc.audit_event("hello", {"k": "v"}, level="error")
    assert called["m"] == "hello"
    assert called["level"] == "error"


def test_audit_command_success(monkeypatch):
    """Vérifie que audit_command loggue bien les breadcrumbs et events en cas de succès."""
    calls = {}

    def fake_breadcrumb(category, message, data):
        calls["breadcrumb"] = (category, message, data)

    def fake_event(message, data=None, level=None):
        calls["event"] = (message, data, level)

    monkeypatch.setattr(ad, "audit_breadcrumb", fake_breadcrumb)
    monkeypatch.setattr(ad, "audit_event", fake_event)

    @ad.audit_command(category="test", action="do_something")
    def my_func(x, y=0):
        return x + y

    result = my_func(2, y=3)

    # Vérifie que la fonction renvoie bien le résultat
    assert result == 5

    # Vérifie que breadcrumb a été appelé
    assert calls["breadcrumb"][0] == "test"
    assert "do_something: start" in calls["breadcrumb"][1]

    # Vérifie que l'event ok a été envoyé
    assert "do_something: ok" in calls["event"][0]
    assert calls["event"][2] == "info"


def test_audit_command_failure(monkeypatch, caplog):
    """Vérifie que audit_command loggue bien les breadcrumbs et events en cas d'erreur."""
    calls = {}

    def fake_breadcrumb(category, message, data):
        calls["breadcrumb"] = (category, message, data)

    def fake_event(message, data=None, level=None):
        calls.setdefault("events", []).append((message, data, level))

    class DummyLogger:
        """Logger factice pour capturer les appels."""

        def error(self, *args, **kwargs):
            """Capture les appels à error."""
            calls["logger"] = "error called"

    monkeypatch.setattr(ad, "audit_breadcrumb", fake_breadcrumb)
    monkeypatch.setattr(ad, "audit_event", fake_event)
    monkeypatch.setattr(ad, "get_audit_logger", lambda: DummyLogger())

    @ad.audit_command(category="test", action="fail_action")
    def my_func(_):
        raise ValueError("boom")

    with pytest.raises(ValueError):
        my_func(1)

    # Vérifie que breadcrumb a été posé avant l'erreur
    assert "fail_action: start" in calls["breadcrumb"][1]

    # Vérifie que l'event "error" a été envoyé
    error_event = [e for e in calls["events"] if "error" in e[0]]
    assert error_event, "aucun event error trouvé"
    assert error_event[0][2] == "error"

    # Vérifie que le logger a bien été appelé
    assert calls["logger"] == "error called"
