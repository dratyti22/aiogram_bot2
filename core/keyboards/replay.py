from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_admin():
    kb = ReplyKeyboardBuilder()
    kb.button(text='Добавить товар', callback_data='add_product_admin')
    kb.button(text='Удалить товар', callback_data='deleted_product_admin')
    kb.button(text='Посмотреть товар в категории')
    kb.button(text='Создать купон', callback_data='create_coupons_admin')
    kb.button(text='Удалить купон', callback_data='deleted_coupons_admin')
    kb.button(text='Посмотреть все купоны', callback_data='display_coupons_admin')
    kb.button(text='Сделать рассылку', callback_data='mailing_admin')
    kb.adjust(2, 1, 2, 1)
    return kb.as_markup(resize_keyboard=True)
