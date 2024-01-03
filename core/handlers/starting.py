from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import os

from core.keyboards.inline import start_inline, catalog_inline, profile_inline, free_top_up_inline, \
    more_information_inline
from core.keyboards.commands import command_bot
from core.keyboards.replay import reply_admin
from core.database.db_user_id import start_user_id_db
from core.database.db_user_balance import create_user_id_and_balance, display_balance
from core.database.db_products_create import create_brawl_stars_db, create_clash_royale_db, create_clash_of_clans_db, \
    create_pubg_mobaile_db, create_codm_db
from core.database.db_coupons import create_coupons

router = Router()


@router.message(Command('start'))
async def start_bot_command(message: Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(text='Ты админ', reply_markup=reply_admin())
    await create_coupons()
    await create_brawl_stars_db()
    await create_clash_royale_db()
    await create_clash_of_clans_db()
    await create_pubg_mobaile_db()
    await create_codm_db()
    await start_user_id_db(message.from_user.id)
    await create_user_id_and_balance(message.from_user.id)
    await command_bot(message.bot)
    await message.answer(
        text='Добро пожаловать в магазин игр! Здесь вы найдете широкий ассортимент игр для всех желаний и интересов.',
        reply_markup=start_inline())


@router.callback_query(F.data == 'catalog')
async def get_catalog(callback: CallbackQuery):
    await callback.bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                         reply_markup=catalog_inline(),
                                         text='Каталог игр')


@router.callback_query(F.data == 'profile')
async def get_profile(callback: CallbackQuery):
    entries = await display_balance(callback.from_user.id)
    if entries:
        balance, _ = entries
        await callback.bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                             reply_markup=profile_inline(),
                                             text=f'Ваш баланс: {balance}₽')


@router.callback_query(F.data == 'free_top_up')
async def get_free_top_up(callback_query: CallbackQuery):
    entries = await display_balance(callback_query.from_user.id)
    if entries:
        balance, _ = entries
        await callback_query.bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=free_top_up_inline(),
            text=f'Ваш баланс: {balance}₽\nВы можете пополнить свой баланс с помощью реферальной программы или промокода'
        )


@router.callback_query(F.data == 'more_information')
async def get_more_information(callback_query: CallbackQuery):
    await callback_query.bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                               message_id=callback_query.message.message_id,
                                               reply_markup=more_information_inline(),
                                               text='Дополнительная информация по кнопкам ниже')


@router.callback_query(F.data == 'back')
async def get_back(callback: CallbackQuery):
    await callback.bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                         reply_markup=start_inline(),
                                         text='Добро пожаловать в магазин игр!\
                                          Здесь вы найдете широкий ассортимент игр для всех желаний и интересов.')
