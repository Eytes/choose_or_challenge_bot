import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from .commands import register_user_command, bot_commands
from .config import config


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    bot = Bot(token=config.token.get_secret_value())
    dp = Dispatcher()

    await bot.set_my_commands(
        [
            BotCommand(command=cmd.command, description=cmd.description)
            for cmd in bot_commands
        ]
    )
    register_user_command(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
