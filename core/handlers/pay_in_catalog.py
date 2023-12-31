from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from time import ctime
import random

from core.database.db_products_create import display_product_pay_in_catalog
from core.keyboards.inline import back_pay_in_catalog_inline, start_inline, pay_in_catalog_product_inline
from core.handlers.state import EmailState
from core.database.db_orders import save_orders_db

router = Router()


@router.callback_query(F.data.startswith('product_'))
async def get_pay_in_catalog_product(callback: CallbackQuery, bot: Bot, state: FSMContext):
    entries = await display_product_pay_in_catalog(callback.data)
    await state.update_data(db_name=callback.data)
    text = ' '.join(f'Покупка товара:\nНазвание: {entry[0]}\nЦена: {entry[1]}\n'
                    f'Что бы купить товар пришлите email на котором зарегетрирован аккаунт' for entry in entries)
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text=text, reply_markup=back_pay_in_catalog_inline())
    await state.set_state(EmailState.EMAIL)


@router.message(EmailState.EMAIL)
async def get_email(message: Message, state: FSMContext):
    data = await state.get_data()
    entries = await display_product_pay_in_catalog(str(data['db_name']))
    if '@' in message.text:
        name_price_list = ((entry[0], entry[1]) for entry in entries)
        name, price = next(name_price_list)
        id_product = ''.join(
            random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()', k=40))
        time = ctime()
        email = message.text
        text = ''.join(f'Информация о заказе:\n'
                       f'Id: {id_product}\n'
                       f'Time: {time}\n'
                       f'Товар {name}\n'
                       f'Цена: {price}\n'
                       f'Почта: {email}\n'
                       f'Спасибо за покупку!')
        await message.answer(text=text, reply_markup=pay_in_catalog_product_inline())
        await save_orders_db(name_products=name, price_products=price, time_products=time, id_products=id_product,
                             email_products=email)
        await state.clear()
    else:
        await message.answer(text='Неправильно указана почта, напишите еще раз.\nПочта должна быть в таком формате:\nqaz@gg.ru')


@router.callback_query(F.data == 'exit_in_menu')
async def get_exit_in_manu(callback: CallbackQuery):
    await (callback.bot.edit_message_text(
        chat_id=callback.message.chat.id, message_id=callback.message.message_id,
        text='Добро пожаловать в магазин игр! Здесь вы найдете широкий ассортимент игр для всех желаний и интересов.',
        reply_markup=start_inline()))
