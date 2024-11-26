from aiogram import Dispatcher

from app.handlers.report import setup_report
from app.handlers.start import setup_start
from app.handlers.unknown_text import setup_unknown_text


def setup_handlers(dp: Dispatcher) -> None:
    setup_start(dp)
    setup_report(dp)
    setup_unknown_text(dp)


__all__ = ["setup_handlers"]
