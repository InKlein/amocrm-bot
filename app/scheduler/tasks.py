import os

from aiogram import Bot

from app.services.amocrm import fetch_revenue_data
from app.services.report import get_report_message_text


async def send_report(bot: Bot) -> None:
    crm_data = await fetch_revenue_data()
    text = await get_report_message_text(crm_data)
    admin_id = os.getenv("ADMIN_ID")
    if not admin_id:
        raise ValueError("ADMIN_ID environment variable is not set")
    await bot.send_message(chat_id=admin_id, text=text)
