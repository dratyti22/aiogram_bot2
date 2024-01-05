from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from core.keyboards.inline import orders_inline
from core.database.db_orders import display_orders_id_db
from core.keyboards.inline import menu_back_inline, start_inline

router = Router()


@router.callback_query(F.data == 'my_orders')
async def get_my_orders(call: CallbackQuery, bot: Bot):
    await bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text='Заказы:',
                                reply_markup=orders_inline())


@router.callback_query(F.data.startswith('order_'))
async def get_orders_id(callback: CallbackQuery):
    entries = await display_orders_id_db(callback.data.split('_')[1])

    text = ''.join(
        f'Name: {entry[0]}\nPrice: {entry[1]}\nTime: {entry[2]}\nId: {entry[3]}'
        for entry in entries
    )
    await callback.bot.edit_message_text(
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        text=text,
        reply_markup=menu_back_inline()
    )


@router.callback_query(F.data == 'menu_back')
async def get_menu_back(callback: CallbackQuery):
    await callback.bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                         text='Добро пожаловать в магазин игр! Здесь вы найдете широкий ассортимент игр для всех желаний и интересов.',
                                         reply_markup=start_inline())
