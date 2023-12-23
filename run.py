from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
import asyncio
import logging

from core.handlers import starting, catalog_games, create_product


async def starting_bot(bot: Bot):
    await bot.send_message(int(os.getenv('ADMIN_ID')), 'Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(int(os.getenv('ADMIN_ID')), 'Бот остановлен')


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    dp = Dispatcher()

    dp.startup.register(starting_bot)
    dp.shutdown.register(stop_bot)

    dp.include_routers(starting.router, catalog_games.router, create_product.router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
