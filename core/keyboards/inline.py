from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core.database.db_orders import display_orders_db


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


def catalog_inline_admin():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Brawl Stars', callback_data='brawl_stars_admin'),
        ],
        [
            InlineKeyboardButton(text='Clash Royale', callback_data='clash_royale_admin'),
            InlineKeyboardButton(text='Clash of Clans', callback_data='clash_of_clans_admin')
        ],
        [
            InlineKeyboardButton(text='PUBG mobaile', callback_data='pubg_mobaile_admin'),
            InlineKeyboardButton(text='CODM', callback_data='codm_admin')
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
            InlineKeyboardButton(text='Мои покупки', callback_data='my_orders')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back')
        ]
    ])
    return kb


def free_top_up_inline():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Промокоды', callback_data='coupons')
        ],
        [
            InlineKeyboardButton(text='Реферальная программа', callback_data='referral_program')
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


def get_referral_program_inline():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Изменить ссылку', callback_data='change_link')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back_referral_program_catalog')
        ]
    ])
    return kb


def get_coupons_inline():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='back_referral_program_catalog')
        ]
    ])
    return kb


def back_pay_in_catalog_inline():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='❌Отмена', callback_data='exit_in_menu')
        ]
    ])
    return kb


def pay_in_catalog_product_inline():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='платить', url='https://www.youtube.com/')
        ],
        [
            InlineKeyboardButton(text='Проверить платеж', callback_data='check_payment')
        ],
        [
            InlineKeyboardButton(text='Изсенить почту', callback_data='change_email')
        ],
        [
            InlineKeyboardButton(text='Обновить', callback_data='updata_pay_product')
        ],
        [
            InlineKeyboardButton(text='Заказы', callback_data='my_orders')
        ]
    ])
    return kb


def orders_inline():
    entries = display_orders_db()
    if len(entries) > 0:
        inline_buttons = [
            [
                InlineKeyboardButton(
                    text=entry[1],
                    callback_data=f'order_{entry[0]}'
                ),
            ] for entry in entries
        ]
        inline_buttons.append([
            InlineKeyboardButton(text='Назад', callback_data='back_catalog')
        ])

        kb = InlineKeyboardMarkup(inline_keyboard=inline_buttons)
        return kb
    else:
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text='Назад', callback_data='back_catalog')
            ]
        ])
        return kb


def menu_back_inline():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='menu_back')
        ]
    ])
    return kb
