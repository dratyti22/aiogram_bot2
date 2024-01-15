from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message, PreCheckoutQuery
from aiogram.fsm.context import FSMContext

from core.keyboards.inline import orders_inline
from core.database.db_orders import display_orders_id_db
from core.keyboards.inline import menu_back_inline, start_inline
from core.handlers.state import TopUpYourBalanceState, AddBalanceState
from core.handlers.pay import payment_for_the_purchase_balance
from core.database.db_user_balance import add_balance

router = Router()


@router.callback_query(F.data == 'my_orders')
async def get_my_orders(call: CallbackQuery, bot: Bot):
    await bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id, text='Заказы:',
                                reply_markup=orders_inline())


@router.callback_query(F.data.startswith('order_'))
async def get_orders_id(callback: CallbackQuery):
    entries = await display_orders_id_db(callback.data.split('_')[1])

    text = ''.join(
        f'Name: {entry[0]}\n💲: {entry[1]}\n⏳: {entry[2]}\n🆔: {entry[3]}\n 🕒 State: {entry[4]}'
        for entry in entries
    )
    await callback.bot.edit_message_text(
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        text=text,
        reply_markup=menu_back_inline()
    )


@router.callback_query(F.data == 'top_up')
async def top_up_your_balance(message: Message, state: FSMContext):
    await message.answer(text='Введите сумму пополнения баланса в рублях, не менее 60 рублей:')
    await state.set_state(TopUpYourBalanceState.NUMBER)


@router.message(TopUpYourBalanceState.NUMBER)
async def add_number_balance(message: Message, state: FSMContext, bot: Bot):
    if message.text and message.text.isdigit():
        await state.update_data(number=int(message.text))
        await payment_for_the_purchase_balance(message, bot, int(message.text))
    else:
        await message.reply(text='Введите сумму пополнения в цифрах')


@router.pre_checkout_query()
async def pre_checkout_query(query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(query.id, ok=True)


@router.message(F.successful_payment)
async def successful_payment(message: Message, state: FSMContext):
    msg = f"платеж на сумму: {message.successful_payment.total_amount // 100}{message.successful_payment.currency} \
    Выполнен"
    await message.answer(msg)
    await state.set_state(AddBalanceState.NUMBER)


@router.message(AddBalanceState.NUMBER)
async def get_add_balance(message: Message, state: FSMContext):
    data = await state.get_data()
    add_balance(message.from_user.id, int(data['number']))
    await state.clear()


@router.callback_query(F.data == 'menu_back')
async def get_menu_back(callback: CallbackQuery):
    await callback.bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                         text='Добро пожаловать в магазин игр! Здесь вы найдете широкий ассортимент игр для всех желаний и интересов.',
                                         reply_markup=start_inline())
