from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery

from core.keyboards.inline_catalog import inline_catalog_brawl_stars
from core.keyboards.inline import catalog_inline

router = Router()


@router.callback_query(F.data == 'brawl_stars')
async def display_brawl_stars_catalog(callback: CallbackQuery, bot: Bot):
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='Выбери товар', reply_markup=inline_catalog_brawl_stars())


@router.callback_query(F.data == 'back_catalog')
async def get_back_catalog(callback: CallbackQuery, bot: Bot):
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text='Каталог игр', reply_markup=catalog_inline())
