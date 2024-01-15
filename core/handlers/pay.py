from aiogram import Bot
from aiogram.types import Message, LabeledPrice
import os


async def payment_for_the_purchase(bot: Bot, message: Message, price: int, name: str):
    invoice_title = 'Покупка товара'
    invoice_description = f'Товар: {name}'
    provider_token = os.getenv('PAYMENT_PROVIDER_TOKEN')
    currency = 'rub'
    payload = 'test'
    labeled_price = LabeledPrice(label='Товар', amount=price * 100)

    await bot.send_invoice(
        chat_id=message.chat.id,
        title=invoice_title,
        description=invoice_description,
        provider_token=provider_token,
        currency=currency,
        payload=payload,
        prices=[labeled_price]
    )


async def payment_for_the_purchase_balance(message: Message, bot: Bot, price: int):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Пополнение баланса',
        description='Пополнение баланса в магазине',
        provider_token=os.getenv("PAYMENT_PROVIDER_TOKEN"),
        currency='rub',
        payload='test',
        prices=[
            LabeledPrice(
                label='Прайс',
                amount=price * 100
            )
        ]
    )
