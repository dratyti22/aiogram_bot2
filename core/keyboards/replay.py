from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_admin():
    kb = ReplyKeyboardBuilder()
    kb.button(text='Добавить товар', callback_data='add_product_admin')
    kb.button(text='Удалить товар', callback_data='deleted_product_admin')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
