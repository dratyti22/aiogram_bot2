from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_inline():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Каталог', callback_data='catalog')
        ],
        [
            InlineKeyboardButton(text='Профиль', callback_data='profile')
        ],
        [
            InlineKeyboardButton(text='Бесплатное пополнение', callback_data='free_top_up'),
            InlineKeyboardButton(text='Больше Информации', callback_data='more_information')
        ]
    ])
    return kb


def catalog_inline():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Brawl Stars', callback_data='brawl_stars'),
        ],
        [
            InlineKeyboardButton(text='Clash Royale', callback_data='Clash_Royale'),
            InlineKeyboardButton(text='Clash of Clans', callback_data='Clash_of_Clans')
        ],
        [
            InlineKeyboardButton(text='PUBG mobaile', callback_data='PUBG_mobaile'),
            InlineKeyboardButton(text='CODM', callback_data='CODM')
        ]
    ])
    return kb


def profile_inline():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Пополнить баланс', callback_data='top_up')
        ],
        [
            InlineKeyboardButton(text='Мои покупки', callback_data='my_purchases')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back')
        ]
    ])
