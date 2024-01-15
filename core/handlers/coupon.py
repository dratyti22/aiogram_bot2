from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import os

from core.handlers.state import AddCouponsState, DeletedCouponsState, TitleState
from core.database.db_coupons import add_coupons, deleted_coupons, display_coupons, get_coupon_details, \
    decrement_coupon_amount
from core.database.db_user_balance import add_balance
from core.keyboards.inline import get_coupons_inline

router = Router()


@router.message(F.text == 'Создать купон')
async def create_add_coupons(message: Message, state: FSMContext):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(text='Введите название купона:')
        await state.set_state(AddCouponsState.NAME)


@router.message(AddCouponsState.NAME)
async def add_coupons_name(message: Message, state: FSMContext):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await state.update_data(name=message.text)
        await message.answer(text='Введите цену купона в рублях:')
        await state.set_state(AddCouponsState.PRICE)


@router.message(AddCouponsState.PRICE)
async def add_coupons_price(message: Message, state: FSMContext):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await state.update_data(price=message.text)
        await message.answer(text='Теперь напишите кол-во купонов:')
        await state.set_state(AddCouponsState.QUANTITY)


@router.message(AddCouponsState.QUANTITY)
async def add_coupons_quantity(message: Message, state: FSMContext):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await state.update_data(quantity=message.text)
        data = await state.get_data()
        await add_coupons(str(data['name']), int(data['price']), int(data['quantity']))
        await message.answer(text='Купоны созданы')
        await state.clear()


@router.message(F.text == 'Удалить купон')
async def deleted_coupons_number(message: Message, state: FSMContext):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(text='Введите id купона:')
        await state.set_state(DeletedCouponsState.ID)


@router.message(DeletedCouponsState.ID)
async def deleted_coupons_id(message: Message, state: FSMContext):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await state.update_data(id=message.text)
        data = await state.get_data()
        await deleted_coupons(int(data['id']))
        await message.answer(text='Купон удален')
        await state.clear()


@router.message(F.text == 'Посмотреть все купоны')
async def display_coupons_admin(message: Message):
    entries = await display_coupons()
    if entries:
        text = '\n'.join(f'id: {entry[0]} name: {entry[1]} price: {entry[2]} quantity: {entry[3]}' for entry in entries)
        await message.answer(text=text)
    else:
        await message.answer(text='Купонов нет')


@router.callback_query(F.data == 'coupons')
async def get_name_coupons(callback: CallbackQuery, state: FSMContext):
    await callback.bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                         text='Напишите название купона:',
                                         reply_markup=get_coupons_inline())
    await state.set_state(TitleState.TITLE)


@router.message(TitleState.TITLE)
async def get_title_state(message: Message, state: FSMContext):
    coupon_name = message.text
    price, amount = await get_coupon_details(coupon_name)
    if price is not None:
        if amount >= 1:
            add_balance(message.from_user.id, price)
            await decrement_coupon_amount(coupon_name)
            message_text = f'Купон "{coupon_name}" успешно использован! Вам добавлена сумма {price} рублей.'
        else:
            message_text = f'Купон "{coupon_name}" больше не доступен.'
    else:
        message_text = f'Купон с названием "{coupon_name}" не найден.'

    await message.answer(
        text=message_text,
        reply_markup=get_coupons_inline()
    )

    await state.clear()
