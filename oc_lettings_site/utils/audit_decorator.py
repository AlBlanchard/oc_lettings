"""Décorateur pour auditer les commandes avec Sentry."""

from functools import wraps
from typing import Callable, Literal
from ..sentry_config import audit_breadcrumb, audit_event, get_audit_logger


def audit_command(
    category: str,
    action: str,
    issue_level_on_error: Literal["error", "critical", "fatal"] = "error",
    event_level_on_success: Literal["info", "warning"] = "info",
):
    """
    Décorateur pour auditer une commande (fonction).
    - category: Catégorie de l'action (ex: "management command")
    - action: Nom de l'action (ex: "import_data")
    - issue_level_on_error: Niveau de l'issue Sentry en cas d'erreur (default: "error")
    - event_level_on_success: Niveau de l'event Sentry en cas de succès (default: "info")
    Comportement :
    - Breadcrumb "start" avant exécution
    - Event "ok" si succès
    - Event + issue Sentry si exception
    """

    def deco(func: Callable):
        """Décorateur effectif.
        param func: La fonction à décorer
        return: La fonction décorée
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            """Fonction décorée avec audit.
            param args: Arguments positionnels
            param kwargs: Arguments nommés
            return: Le résultat de la fonction décorée
            """
            audit_breadcrumb(
                category, f"{action}: start", {"args": str(args), "kwargs": kwargs}
            )
            try:
                result = func(*args, **kwargs)
                audit_event(
                    f"{action}: ok", {"kwargs": kwargs}, level=event_level_on_success
                )
                return result
            except Exception as e:
                # Event + issue (via level error/critical/fatal)
                audit_event(
                    f"{action}: error",
                    {"kwargs": kwargs, "error": str(e)},
                    level=issue_level_on_error,
                )
                get_audit_logger().error("%s failed: %s", action, e, exc_info=True)
                raise

        return wrapper

    return deco
