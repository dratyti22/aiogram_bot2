from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.utils.deep_linking import create_start_link

from core.database.db_referral_program import create_referral_program_db, display_referral_program_db
from core.keyboards.inline import get_referral_program_inline
from core.handlers.starting import get_free_top_up

router = Router()


@router.callback_query(F.data == 'referral_program')
async def set_referral_program(callback: CallbackQuery):
    link = await create_start_link(callback.bot, str(callback.from_user.id))
    await create_referral_program_db(int(callback.from_user.id), str(link))
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
