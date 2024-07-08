from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import (
    BotCommand,
    BotCommandScopeChat,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllPrivateChats,
)

from app.bot.utils.texts import SUPPORTED_LANGUAGES
from app.config import Config


async def setup(bot: Bot, config: Config) -> None:
    """
    Set up bot commands for various scopes and languages.

    :param bot: The Bot object.
    :param config: The Config object.
    """
    # Define bot commands for different languages
    commands = {
        "en": [
            BotCommand(command="start", description="Restart bot"),
        ],
        "es": [
            BotCommand(command="start", description="Reiniciar el bot"),
        ]
    }

    if len(SUPPORTED_LANGUAGES) > 1:
        # If there are more than one supported language, add commands for changing the language
        commands["en"].append(
            BotCommand(command="language", description="Change language"),
        )
        commands["es"].append(
            BotCommand(command="language", description="Cambiar idioma"),
        )

    group_commands = {
        "en": [
            BotCommand(command="ban", description="Block/Unblock a user"),
            BotCommand(command="silent", description="Activate/Deactivate silent Mode"),
            BotCommand(command="information", description="User information"),
        ],
        "es": [
            BotCommand(command="ban", description="Bloquear/Desbloquear a un usuario"),
            BotCommand(command="silent", description="Activar/Desactivar modo silencioso"),
            BotCommand(command="information", description="Información del usuario"),
        ]
    }

    admin_commands = {
        "en":
            commands["en"].copy() +
            [BotCommand(command="newsletter", description="Newsletter menu")],
        "es":
            commands["es"].copy() +
            [BotCommand(command="newsletter", description="Menú de boletines")],
    }

    try:
        # Set commands for dev or admin in English language
        await bot.set_my_commands(
            commands=admin_commands["en"],
            scope=BotCommandScopeChat(chat_id=config.bot.DEV_ID),
        )
        # Set commands for dev or admin in Spanish language
        await bot.set_my_commands(
            commands=admin_commands["es"],
            scope=BotCommandScopeChat(chat_id=config.bot.DEV_ID),
            language_code="es",
        )
    except TelegramBadRequest:
        raise ValueError(f"Chat with DEV_ID {config.bot.DEV_ID} not found.")

    # Set commands for all private chats in English language
    await bot.set_my_commands(
        commands=commands["en"],
        scope=BotCommandScopeAllPrivateChats(),
    )
    # Set commands for all private chats in Spanish language
    await bot.set_my_commands(
        commands=commands["es"],
        scope=BotCommandScopeAllPrivateChats(),
        language_code="es",
    )
    # Set commands for all group chats in English language
    await bot.set_my_commands(
        commands=group_commands["en"],
        scope=BotCommandScopeAllGroupChats(),
    )
    # Set commands for all group chats in Spanish language
    await bot.set_my_commands(
        commands=group_commands["es"],
        scope=BotCommandScopeAllGroupChats(),
        language_code="es"
    )


async def delete(bot: Bot, config: Config) -> None:
    """
    Delete bot commands for various scopes and languages.

    :param config: The Config object.
    :param bot: The Bot object.
    """

    try:
        # Delete commands for dev or admin in any language
        await bot.delete_my_commands(
            scope=BotCommandScopeChat(chat_id=config.bot.DEV_ID),
        )
        # Delete commands for dev or admin in Spanish language
        await bot.delete_my_commands(
            scope=BotCommandScopeChat(chat_id=config.bot.DEV_ID),
            language_code="es",
        )
    except TelegramBadRequest:
        raise ValueError(f"Chat with DEV_ID {config.bot.DEV_ID} not found.")

    # Delete commands for all private chats in any language
    await bot.delete_my_commands(
        scope=BotCommandScopeAllPrivateChats(),
    )
    # Delete commands for all private chats in Spanish language
    await bot.delete_my_commands(
        scope=BotCommandScopeAllPrivateChats(),
        language_code="es",
    )
    # Delete commands for all group chats in any language
    await bot.delete_my_commands(
        scope=BotCommandScopeAllGroupChats(),
    )
    # Delete commands for all group chats in Spanish language
    await bot.delete_my_commands(
        scope=BotCommandScopeAllGroupChats(),
        language_code="es",
    )
