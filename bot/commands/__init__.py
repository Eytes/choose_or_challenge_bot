__all__ = [
    "register_user_command",
    "bot_commands",
]

from aiogram import Router
from aiogram.filters import CommandStart, Command

from .bot_commands_description import bot_commands
from .help import help_command
from .start import start


def register_user_command(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=["help"]))
