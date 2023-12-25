from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from core.database.db_products_create import display_brawl_stars_db, display_clash_of_clans_db, \
    display_pubg_mobaile_db, display_clash_royale_db, display_codm_db


def inline_catalog_brawl_stars():
    entries = display_brawl_stars_db()
    if len(entries) > 0:
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
    else:
        return inline_catalog_back()


def inline_catalog_clash_of_clans():
    entries = display_clash_of_clans_db()

    if len(entries) > 0:
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
    else:
        return inline_catalog_back()


def inline_catalog_pubg_mobaile():
    entries = display_pubg_mobaile_db()

    if len(entries) > 0:
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
    else:
        return inline_catalog_back()


def inline_catalog_clash_royale():
    entries = display_clash_royale_db()

    if len(entries) > 0:
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
    else:
        return inline_catalog_back()


def inline_catalog_codm():
    entries = display_codm_db()

    if len(entries) > 0:
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
    else:
        return inline_catalog_back()


def inline_catalog_back():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='back_catalog')
        ]
    ])
    return kb
