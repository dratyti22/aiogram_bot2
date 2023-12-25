from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
import os

from core.keyboards.inline import catalog_inline_admin
from core.handlers.state import AddProductAdminState, AddProductAdminBsState, AddProductAdminCodmState, \
    AddProductAdminCocState, AddProductAdminCrState, AddProductAdminPmState, DeletedProductAdminState
from core.database.db_products_add import add_product_brawl_stars_db, add_product_codm_db, \
    add_product_clash_of_clans_db, add_product_clash_royale_db, add_product_pubg_mobaile_db
from core.database.db_product_deleted import deleted_products_db

router = Router()


@router.message(F.text == 'Удалить товар')
async def get_deleted_product_admin(message: Message, state: FSMContext):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(text='Выбери категорию игр:', reply_markup=catalog_inline_admin())
        await state.set_state(DeletedProductAdminState.MAIN)
    else:
        await message.answer(text='Ты не админnЗабудь эту команду!')
        await state.clear()


@router.callback_query(DeletedProductAdminState.MAIN)
async def get_main_catalog(callback: CallbackQuery, state: FSMContext):
    if callback.data:
        await state.update_data(category=callback.data)
        await callback.message.answer(text='Напиши айди товара, который хочешь удалить:')
        await state.set_state(DeletedProductAdminState.ID)
    else:
        await callback.message.answer(text='Необходимо выбрать категорию')
        await state.clear()


@router.message(DeletedProductAdminState.ID)
async def get_deleted_product_id(message: Message, state: FSMContext):
    if message.text:
        data = await state.get_data()
        category = data.get('category')
        if message.text.isdigit():
            await message.answer('Товар удален')
            deleted_products_db(category, int(message.text))
            await state.clear()
        else:
            await message.answer(text='Надо ввести число.nНапиши число')
            await state.set_state(DeletedProductAdminState.ID)
    else:
        await message.answer(text='Необходимо ввести айди товара')
        await state.set_state(DeletedProductAdminState.ID)


@router.message(F.text == 'Добавить товар')
async def get_add_product_admin(message: Message, state: FSMContext):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(text='Выбери категорию игр:', reply_markup=catalog_inline_admin())
        await state.set_state(AddProductAdminState.MAIN)
    else:
        await message.answer(text='Ты не админ\nЗабудь эту команду!')


@router.callback_query(AddProductAdminState.MAIN)
async def add_product_brawl_stars(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'brawl_stars_admin':
        await callback.message.answer(text='Вы выбрали категорию: Brawl Stars\nНапиши название товара:')
        await state.set_state(AddProductAdminBsState.NAME)
    elif callback.data == 'clash_royale_admin':
        await callback.message.answer(text='Вы выбрали категорию: Clash Royale\nНапиши название товара:')
        await state.set_state(AddProductAdminCrState.NAME)
    elif callback.data == 'clash_of_clans_admin':
        await callback.message.answer(text='Вы выбрали категорию: Clash of Clans\nНапиши название товара:')
        await state.set_state(AddProductAdminCocState.NAME)
    elif callback.data == 'pubg_mobaile_admin':
        await callback.message.answer(text='Вы выбрали категорию: PUBG mobaile\nНапиши название товара:')
        await state.set_state(AddProductAdminPmState.NAME)
    elif callback.data == 'codm_admin':
        await callback.message.answer(text='Вы выбрали категорию: CODM\nНапиши название товара:')
        await state.set_state(AddProductAdminCodmState.NAME)


# Brawl Stars
@router.message(AddProductAdminBsState.NAME)
async def add_product_brawl_stars_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Напиши цену товара:')
    await state.set_state(AddProductAdminBsState.PRICE)


# Brawl Stars
@router.message(AddProductAdminBsState.PRICE)
async def add_product_brawl_stars_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    await add_product_brawl_stars_db(str(data['name']), int(data['price']))
    await message.answer(text='Товар добавлен')
    await state.clear()


# CODM
@router.message(AddProductAdminCodmState.NAME)
async def add_product_brawl_stars_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Напиши цену товара:')
    await state.set_state(AddProductAdminCodmState.PRICE)


# CODM
@router.message(AddProductAdminCodmState.PRICE)
async def add_product_brawl_stars_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    await add_product_codm_db(str(data['name']), int(data['price']))
    await message.answer(text='Товар добавлен')
    await state.clear()


# CLASH OF CLANS
@router.message(AddProductAdminCocState.NAME)
async def add_product_brawl_stars_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Напиши цену товара:')
    await state.set_state(AddProductAdminCocState.PRICE)


# CLASH OF CLANS
@router.message(AddProductAdminCocState.PRICE)
async def add_product_brawl_stars_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    await add_product_clash_of_clans_db(str(data['name']), int(data['price']))
    await message.answer(text='Товар добавлен')
    await state.clear()


# ClASH ROYALE
@router.message(AddProductAdminCrState.NAME)
async def add_product_brawl_stars_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Напиши цену товара:')
    await state.set_state(AddProductAdminCrState.PRICE)


# ClASH ROYALE
@router.message(AddProductAdminCrState.PRICE)
async def add_product_brawl_stars_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    await add_product_clash_royale_db(str(data['name']), int(data['price']))
    await message.answer(text='Товар добавлен')
    await state.clear()


# PUBG MOBAILE
@router.message(AddProductAdminPmState.NAME)
async def add_product_brawl_stars_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Напиши цену товара:')
    await state.set_state(AddProductAdminPmState.PRICE)


# PUBG MOBAILE
@router.message(AddProductAdminPmState.PRICE)
async def add_product_brawl_stars_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    await add_product_pubg_mobaile_db(str(data['name']), int(data['price']))
    await message.answer(text='Товар добавлен')
    await state.clear()
