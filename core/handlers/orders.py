from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from core.keyboards.inline import orders_inline
from core.database.db_orders import display_orders_id_db
from core.keyboards.inline_catalog import inline_catalog_back

router = Router()


@router.callback_query(F.data == 'my_orders')
async def get_my_orders(call: CallbackQuery, bot: Bot):
    await bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text='Заказы:',
                                reply_markup=orders_inline())


@router.callback_query(F.data.startswith('orders_'))
async def get_orders_id(callback: CallbackQuery):
    entries = display_orders_id_db(callback.data)
    text = ''.join(f'Name: {entry[0]}\nPrice: {entry[1]}\nTime: {entry[2]}\nId: {entry[3]}' for entry in entries)
    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id,
                                         text=text, reply_markup=inline_catalog_back())
