from aiogram import types
from aiogram.filters import CommandObject

from . import bot_commands


async def help_command(message: types.Message, command: CommandObject) -> None:
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                await message.answer(
                    f"{cmd.command} - {cmd.description}\n\n{cmd.detailed}"
                )
                return None
        await message.answer(f"Команда {command.args} не найдена")

    await message.answer(
        f"Помощь и справка о боте\n"
        f"Для получения справки о команде введите /help <команда>\n"
    )
