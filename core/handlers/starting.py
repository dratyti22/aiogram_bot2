from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from core.handlers.text import text_start
from core.keyboards.inline import start_inline, catalog_inline
from core.keyboards.commands import command_bot

router = Router()


@router.message(Command('start'))
async def start_bot_command(message: Message):
    await command_bot(message.bot)
    await message.answer(text=text_start, reply_markup=start_inline())


@router.callback_query(F.data == 'catalog')
async def get_catalog(callback: CallbackQuery):
    await callback.bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                         reply_markup=catalog_inline(),
                                         text='Каталог игр')
