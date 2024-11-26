from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.scheduler.tasks import send_report


async def setup_scheduler(bot: Bot) -> None:
    scheduler = AsyncIOScheduler()
    scheduler.configure(timezone="Europe/Moscow")
    scheduler.add_job(send_report, 'cron', hour=20, minute=0, id="send_report", args=[bot])
    scheduler.start()