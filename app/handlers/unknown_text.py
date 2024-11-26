from aiogram import Dispatcher, Router, F
from aiogram.types import Message


async def unknown_text(message: Message) -> None:
    await message.answer("Sorry, I didn't understand.")


def setup_unknown_text(dp: Dispatcher) -> None:
    router = Router(name=__name__)
    router.message.register(unknown_text)
    dp.include_router(router)
