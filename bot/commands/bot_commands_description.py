from typing import NamedTuple

DefaultBotCommand = NamedTuple(
    "DefaultBotCommand",
    [("command", str), ("description", str), ("detailed", str)],
)

bot_commands = (
    DefaultBotCommand(
        "start",
        "Начало работы с ботом",
        "Команда, чтобы начать работу с ботом",
    ),
    DefaultBotCommand(
        "help",
        "Помощь и справка",
        "Команда для вывода списка команд и описания этих команд",
    ),
)
