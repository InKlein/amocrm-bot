from aiogram import Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.amocrm import fetch_revenue_data
from app.services.report import get_report_message_text


async def report_cmd(message: Message) -> None:
    crm_data = await fetch_revenue_data()
    text = await get_report_message_text(crm_data)
    await message.answer(text)


def setup_report(dp: Dispatcher) -> None:
    router = Router(name=__name__)
    router.message.register(report_cmd, Command("report"))

    dp.include_router(router)
