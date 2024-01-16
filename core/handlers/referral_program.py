from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.utils.deep_linking import create_start_link
from aiogram.fsm.context import FSMContext

from core.database.db_referral_program import add_referral_program_db, display_referral_program_db, \
    change_the_link_db
from core.keyboards.inline import get_referral_program_inline, menu_back_inline
from core.handlers.starting import get_free_top_up
from core.handlers.state import ChangeLinkState

router = Router()


@router.callback_query(F.data == 'referral_program')
async def set_referral_program(callback: CallbackQuery):
    link = await create_start_link(callback.bot, str(callback.from_user.id))
    await add_referral_program_db(int(callback.from_user.id), str(link))
    entries = await display_referral_program_db()
    text = ' '.join(f'Ваша реферальная ссылка: {entry[1]}\nКоличество приглашенных людей: {entry[3]}\n'
                    f'Процент с покупки реферала: 10%\n'
                    f'Баланс можно увеличить приглашая людей' for entry in entries)
    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id,
                                         text=text,
                                         reply_markup=get_referral_program_inline())


@router.callback_query(F.data == 'back_referral_program_catalog')
async def get_back_referral_program(callback_query: CallbackQuery):
    await get_free_top_up(callback_query)


@router.callback_query(F.data == 'change_link')
async def get_change_link(callback: CallbackQuery, state: FSMContext):
    await callback.bot.edit_message_text(message_id=callback.message.message_id, chat_id=callback.message.chat.id,
                                         text='Напишите новую ссылку, которую вы хотите указать:',
                                         reply_markup=menu_back_inline())
    await state.set_state(ChangeLinkState.LINK)


@router.message(ChangeLinkState.LINK)
async def set_change_link(message: Message, state: FSMContext, bot: Bot):
    new_link = await create_start_link(bot, message.text)
    await change_the_link_db(message.from_user.id, str(new_link))
    await message.answer('Ссылка успешно изменена', reply_markup=menu_back_inline())
    await state.clear()
