from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery
from aiogram.fsm.context import FSMContext
import datetime
import random

from core.database.db_products_create import display_product_pay_in_catalog
from core.keyboards.inline import back_pay_in_catalog_inline, start_inline, pay_in_catalog_product_inline, \
    pay_in_catalog_product_inline_free
from core.handlers.state import EmailState
from core.database.db_orders import save_orders_db, change_email_db
from core.handlers.pay import payment_for_the_purchase
from core.database.db_user_balance import subtract_balance, display_balance

router = Router()


@router.callback_query(F.data.startswith('product_'))
async def get_pay_in_catalog_product(callback: CallbackQuery, bot: Bot, state: FSMContext):
    entries = await display_product_pay_in_catalog(callback.data)
    await state.update_data(db_name=callback.data)
    text = ' '.join(f'Покупка товара:\nНазвание: {entry[0]}\nЦена: {entry[1]}\n'
                    f'Чтобы купить товар, отправьте email, на котором зарегистрирован аккаунт' for entry in entries)
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                text=text, reply_markup=back_pay_in_catalog_inline())
    await state.set_state(EmailState.EMAIL)


@router.message(EmailState.EMAIL)
async def get_email(message: Message, state: FSMContext):
    data = await state.get_data()
    entries = await display_product_pay_in_catalog(str(data['db_name']))
    db_balance = display_balance(message.from_user.id)
    balance = db_balance[0]
    if '@' in message.text and message.text.endswith('.com'):
        name_price_list = ((entry[0], entry[1]) for entry in entries)
        name, price = next(name_price_list)
        id_product = ''.join(
            random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()', k=40))
        time = datetime.datetime.now().strftime("%d.%m.%Y")
        email = message.text
        pay_time = 'ждет оплаты'
        text = ''.join(f'Информация о заказе:\n'
                       f'🆔: {id_product}\n\n'
                       f'⏳: {time}\n'
                       f'Товар {name}\n'
                       f'💲: {price}\n\n'
                       f'📧: {email}\n'
                       f'🕒 Товар: {pay_time}')
        if balance >= price:
            await message.answer(text=text, reply_markup=pay_in_catalog_product_inline_free())
        else:
            await message.answer(text=text, reply_markup=pay_in_catalog_product_inline())
        await save_orders_db(name_products=name, price_products=price, time_products=time, id_product=id_product,
                             email_products=email, payment_products=pay_time)
        updated_data = {
            'pay_name': name,
            'pay_price': price,
            'pay_id_product': id_product,
            'pay_time': time,

            'pay_pay_time': pay_time
        }
        await state.update_data(**updated_data)
    else:
        await message.reply(text='Неправильно указана почта, напишите еще раз.\n'
                                 'Почта должна быть в таком формате:\nqaz@gg.com')


@router.callback_query(F.data == 'pay_product')
async def get_pay_product(callback_query: CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    await payment_for_the_purchase(bot, callback_query.message, int(data['pay_price']), str(data['pay_name']))


@router.pre_checkout_query()
async def pre_checkout_query(query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(query.id, ok=True)


@router.message(F.successful_payment)
async def successful_payment(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id,
                           text=f'Платеж выполнен на сумму: {message.successful_payment.total_amount // 100}\
    {message.successful_payment.currency}')
    await state.clear()


@router.callback_query(F.data == 'pay_product_free')
async def get_pay_product_free(message: Message, state: FSMContext):
    data = await state.get_data()
    subtract_balance(message.from_user.id, int(data['pay_price']))
    await message.answer('Товар куплен!\nПришлите скрин с покупкой админу, что бы он связался с вами')


@router.callback_query(F.data == 'change_email')
async def get_change_email(callback: CallbackQuery, state: FSMContext):
    text = ''.join(f'Отправьте email, на который хотите изменить')
    await callback.bot.send_message(chat_id=callback.message.chat.id,
                                    text=text, reply_markup=back_pay_in_catalog_inline())
    await state.set_state(EmailState.ChangeEmail)


@router.message(EmailState.ChangeEmail)
async def change_email_pay_in_catalog(message: Message, state: FSMContext):
    data = await state.get_data()
    balance_entry =display_balance(message.from_user.id)
    balance = balance_entry[0]
    if '@' in message.text and message.text.endswith('.com'):
        change_email_db(data['pay_id_product'], message.text)
        text = (
            "Информация о заказе:\n"
            f"🆔: {data['pay_id_product']}\n\n"
            f"⏳: {data['pay_time']}\n"
            f"Товар: {data['pay_name']}\n"
            f"💲: {data['pay_price']}\n\n"
            f"📧: {message.text}\n"
            f"🕒 Товар: {data['pay_pay_time']}"
        )
        if balance >= data['pay_price']:
            await message.answer(text=text, reply_markup=pay_in_catalog_product_inline_free())
        else:
            await message.answer(text=text, reply_markup=pay_in_catalog_product_inline())
    else:
        await message.reply(
            text='Неправильно указана почта, напишите еще раз.nПочта должна быть в таком формате: qaz@gg.com')


@router.callback_query(F.data == 'check_payment')
async def get_check_payment(callback: CallbackQuery, state: FSMContext):
    if callback.message.successful_payment:
        await callback.bot.send_message(chat_id=callback.message.chat.id, text=f'Платеж выполнен на сумму: \
        {callback.message.successful_payment.total_amount // 100}\
        {callback.message.successful_payment.currency}')
        await state.clear()
    else:
        await callback.message.answer(text='Платеж не выполнен!')


@router.callback_query(F.data == 'update_pay_product')
async def get_update_pay_product(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if callback.message.successful_payment:
        data['pay_pay_time'] = 'платеж выполнен'
        await change_email_pay_in_catalog(callback.message, state)
    else:
        await change_email_pay_in_catalog(callback.message, state)


@router.callback_query(F.data == 'exit_in_menu')
async def get_exit_in_manu(callback: CallbackQuery):
    await (callback.bot.edit_message_text(
        chat_id=callback.message.chat.id, message_id=callback.message.message_id,
        text='Добро пожаловать в магазин игр! Здесь вы найдете широкий ассортимент игр для всех желаний и интересов.',
        reply_markup=start_inline()))
