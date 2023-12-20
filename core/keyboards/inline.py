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
