import sys
import asyncio


def pytest_configure():
    # Sous Windows, évite les warnings "There is no current event loop" avec Django
    if sys.platform.startswith("win"):
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        except Exception:
            pass
