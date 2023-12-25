from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery

from core.keyboards.inline_catalog import inline_catalog_brawl_stars, inline_catalog_codm, \
    inline_catalog_clash_royale, inline_catalog_pubg_mobaile, inline_catalog_clash_of_clans
from core.keyboards.inline import catalog_inline

router = Router()


@router.callback_query(F.data == 'brawl_stars')
async def display_brawl_stars_catalog(callback: CallbackQuery, bot: Bot):
    entries = inline_catalog_brawl_stars()

    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='Выбери товар', reply_markup=entries)


@router.callback_query(F.data == 'codm')
async def display_brawl_stars_catalog(callback: CallbackQuery, bot: Bot):
    entries = inline_catalog_codm()

    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='Выбери товар', reply_markup=entries)


@router.callback_query(F.data == 'clash_royale')
async def display_brawl_stars_catalog(callback: CallbackQuery, bot: Bot):
    entries = inline_catalog_clash_royale()

    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='Выбери товар', reply_markup=entries)


@router.callback_query(F.data == 'pubg_mobaile')
async def display_brawl_stars_catalog(callback: CallbackQuery, bot: Bot):
    entries = inline_catalog_pubg_mobaile()

    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='Выбери товар', reply_markup=entries)


@router.callback_query(F.data == 'clash_of_clans')
async def display_brawl_stars_catalog(callback: CallbackQuery, bot: Bot):
    entries = inline_catalog_clash_of_clans()

    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='Выбери товар', reply_markup=entries)


@router.callback_query(F.data == 'back_catalog')
async def get_back_catalog(callback: CallbackQuery, bot: Bot):
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='Каталог игр', reply_markup=catalog_inline())
