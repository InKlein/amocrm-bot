from aiogram import Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message


async def start_cmd(message: Message) -> None:
    await message.answer("Hi!")


def setup_start(dp: Dispatcher) -> None:
    router = Router(name=__name__)
    router.message.register(start_cmd, Command("start"))

    dp.include_router(router)
