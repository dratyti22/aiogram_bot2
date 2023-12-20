from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from core.handlers.text import text_start
from core.keyboards.inline import start_inline, catalog_inline

router = Router()


@router.message(Command('start'))
async def start_bot_command(message: Message):
    await message.answer(text=text_start, reply_markup=start_inline())
