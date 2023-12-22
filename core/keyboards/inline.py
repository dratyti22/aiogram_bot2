from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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
            InlineKeyboardButton(text='Clash Royale', callback_data='clash_royale'),
            InlineKeyboardButton(text='Clash of Clans', callback_data='clash_of_clans')
        ],
        [
            InlineKeyboardButton(text='PUBG mobaile', callback_data='pubg_mobaile'),
            InlineKeyboardButton(text='CODM', callback_data='codm')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back')
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
    return kb


def free_top_up_inline():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Промокоды', callback_data='promocodes')
        ],
        [
            InlineKeyboardButton(text='Реферальная программа', callback_data='referal_program')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back')
        ]
    ])
    return kb


def more_information_inline():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='О нас', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        ],
        [
            InlineKeyboardButton(text='Контакты админа', url='https://t.me/@user_nameeeeeeeeeeee')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back')
        ]
    ])
    return kb
