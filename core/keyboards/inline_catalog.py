from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.database.db_products_create import display_brawl_stars_db


def inline_catalog_brawl_stars():
    entries = display_brawl_stars_db()

    inline_buttons = [
        [
            InlineKeyboardButton(
                text=entry[1],
                callback_data=f'product_{entry[0]}_brawl_stars'
            ),
        ] for entry in entries
    ]
    inline_buttons.append([
        InlineKeyboardButton(text='Назад', callback_data='back_catalog')
    ])

    kb = InlineKeyboardMarkup(inline_keyboard=inline_buttons)
    return kb
