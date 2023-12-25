from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from core.database.db_products_create import display_brawl_stars_db, display_clash_of_clans_db, \
    display_pubg_mobaile_db, display_clash_royale_db, display_codm_db


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


def inline_catalog_clash_of_clans():
    entries = display_clash_of_clans_db()

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


def inline_catalog_pubg_mobaile():
    entries = display_pubg_mobaile_db()

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


def inline_catalog_clash_royale():
    entries = display_clash_royale_db()

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


def inline_catalog_codm():
    entries = display_codm_db()

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
