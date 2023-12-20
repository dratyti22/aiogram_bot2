from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from core.handlers.text import text_start
from core.keyboards.inline import start_inline, catalog_inline, profile_inline, free_top_up_inline, more_information_inline
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


@router.callback_query(F.data == 'profile')
async def get_profile(callback: CallbackQuery):
    await callback.bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                         reply_markup=profile_inline(),
                                         text=f'Ваш баланс: {0}₽')


@router.callback_query(F.data == 'free_top_up')
async def get_free_top_up(callback_query: CallbackQuery):
    await callback_query.bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                               message_id=callback_query.message.message_id,
                                               reply_markup=free_top_up_inline(),
                                               text=f'Ваш баланс: {0}₽\n'
                                                    f'Вы можете пополнить свой баланс с помощью реферальной программы или'
                                                    f' промокода')


@router.callback_query(F.data=='more_information')
async def get_more_information(callback_query: CallbackQuery):
    await callback_query.bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                               message_id=callback_query.message.message_id,
                                               reply_markup=more_information_inline(),
                                               text='Дополнительная информация по кнопкам ниже')


@router.callback_query(F.data == 'back')
async def get_back(callback: CallbackQuery):
    await callback.bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                         reply_markup=start_inline(),
                                         text=text_start)
