from aiogram import Bot
from aiogram.types import BotCommandScopeDefault, BotCommand


async def command_bot(bot: Bot):
    command = [
        BotCommand(
            command='start',
            description='запустить бота'
        )
    ]
    await bot.set_my_commands(command, scope=BotCommandScopeDefault())
