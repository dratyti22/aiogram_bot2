from aiogram import F, Bot, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from core.keyboards.inline import catalog_inline_admin
from core.handlers.state import AddProductAdminState
from core.database.db_products_add import add_product_brawl_stars_db

router = Router()


@router.message(F.text == 'Добавить товар')
async def get_add_product_admin(message: Message, state: FSMContext):
    await message.answer(text='Выбери категорию игр:', reply_markup=catalog_inline_admin())
    await state.set_state(AddProductAdminState.MAIN)


@router.callback_query(F.data == 'brawl_stars_admin', AddProductAdminState.MAIN)
async def add_product_brawl_stars(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Вы выбрали категорию: Brawl Stars\nНапиши название товара:')
    await state.set_state(AddProductAdminState.NAME)


@router.message(AddProductAdminState.NAME)
async def add_product_brawl_stars_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Напиши цену товара:')
    await state.set_state(AddProductAdminState.PRICE)


@router.message(AddProductAdminState.PRICE)
async def add_product_brawl_stars_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    await add_product_brawl_stars_db(str(data['name']), int(data['price']))
    await message.answer(text='Товар добавлен')
    await state.clear()
