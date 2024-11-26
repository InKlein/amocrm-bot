import asyncio
import os

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand
from dotenv import load_dotenv

from app.crm.setup_amocrm import setup_amocrm
from app.handlers import setup_handlers
from app.scheduler import setup_scheduler


async def set_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command="/start", description="start"),
        BotCommand(command="/report", description="report"),

    ]
    await bot.set_my_commands(commands)


async def main() -> None:
    load_dotenv()
    token = os.getenv('TOKEN')
    if not token:
        raise ValueError("TOKEN env variable is not set")

    dp = Dispatcher()
    bot = Bot(
        token=token,
        default=DefaultBotProperties(parse_mode='HTML')
    )

    setup_handlers(dp)
    await set_commands(bot)

    await setup_scheduler(bot)
    setup_amocrm()
    print("started")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
