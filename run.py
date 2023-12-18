from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
import asyncio


async def start_bot(bot: Bot):
    await bot.send_message(int(os.getenv('ADMIN_ID')), 'Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(int(os.getenv('ADMIN_ID')), 'Бот остановлен')


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()

    dp.startup(start_bot)
    dp.shutdown(stop_bot)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
