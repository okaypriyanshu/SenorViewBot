from abc import abstractmethod, ABCMeta

# Add other languages and their corresponding codes as needed.
# You can also keep only one language by removing the line with the unwanted language.
SUPPORTED_LANGUAGES = {
    "es": "🇪🇸 Español",
    "en": "🇬🇧 English",
}


class Text(metaclass=ABCMeta):
    """
    Abstract base class for handling text data in different languages.
    """

    def __init__(self, language_code: str) -> None:
        """
        Initializes the Text instance with the specified language code.

        :param language_code: The language code (e.g., "es" or "en").
        """
        self.language_code = language_code if language_code in SUPPORTED_LANGUAGES.keys() else "en"

    @property
    @abstractmethod
    def data(self) -> dict:
        """
        Abstract property to be implemented by subclasses. Represents the language-specific text data.

        :return: Dictionary containing language-specific text data.
        """
        raise NotImplementedError

    def get(self, code: str) -> str:
        """
        Retrieves the text corresponding to the provided code in the current language.

        :param code: The code associated with the desired text.
        :return: The text in the current language.
        """
        return self.data[self.language_code][code]


class TextMessage(Text):
    """
    Subclass of Text for managing text messages in different languages.
    """

    @property
    def data(self) -> dict:
        """
        Provides language-specific text data for text messages.

        :return: Dictionary containing language-specific text data for text messages.
        """
        return {
            "en": {
                "select_language": "👋 <b>Hello</b>, {full_name}!\n\nSelect language:",
                "change_language": "<b>Select language:</b>",
                "main_menu": "<b>Write your question</b>, and we will answer you as soon as possible:",
                "message_sent": "<b>Message sent!</b> Expect a response.",
                "message_edited": (
                    "<b>The message was edited only in your chat.</b> "
                    "To send an edited message, send it as a new message."
                ),
                "user_started_bot": (
                    "<b>User {name} started the bot!</b>\n\n"
                    "List of available commands:\n\n"
                    "• /ban\n"
                    "Block/Unblock user"
                    "<blockquote>Block the user if you do not want to receive messages from him.</blockquote>\n\n"
                    "• /silent\n"
                    "Activate/Deactivate silent mode"
                    "<blockquote>When silent mode is enabled, messages are not sent to the user.</blockquote>\n\n"
                    "• /information\n"
                    "User information"
                    "<blockquote>Receive a message with basic information about the user.</blockquote>"
                ),
                "user_restarted_bot": "<b>User {name} restarted the bot!</b>",
                "user_stopped_bot": "<b>User {name} stopped the bot!</b>",
                "user_blocked": "<b>User blocked!</b> Messages from the user are not accepted.",
                "user_unblocked": "<b>User unblocked!</b> Messages from the user are being accepted again.",
                "blocked_by_user": "<b>Message not sent!</b> The bot has been blocked by the user.",
                "user_information": (
                    "<b>ID:</b>\n"
                    "- <code>{id}</code>\n"
                    "<b>Name:</b>\n"
                    "- {full_name}\n"
                    "<b>Status:</b>\n"
                    "- {state}\n"
                    "<b>Username:</b>\n"
                    "- {username}\n"
                    "<b>Blocked:</b>\n"
                    "- {is_banned}\n"
                    "<b>Registration date:</b>\n"
                    "- {created_at}"
                ),
                "message_not_sent": "<b>Message not sent!</b> An unexpected error occurred.",
                "message_sent_to_user": "<b>Message sent to user!</b>",
                "silent_mode_enabled": (
                    "<b>Silent mode activated!</b> Messages will not be delivered to the user."
                ),
                "silent_mode_disabled": (
                    "<b>Silent mode deactivated!</b> The user will receive all messages."
                ),
            },
            "es": {
                "select_language": "👋 <b>Hola</b>, {full_name}!\n\nSeleccione el idioma:",
                "change_language": "<b>Seleccione el idioma:</b>",
                "main_menu": "<b>Escriba su pregunta</b>, y le responderemos lo antes posible:",
                "message_sent": "<b>Mensaje enviado!</b> Espere una respuesta.",
                "message_edited": (
                    "<b>El mensaje fue editado solo en su chat.</b> "
                    "Para enviar un mensaje editado, envíelo como un nuevo mensaje."
                ),
                "user_started_bot": (
                    "<b>El usuario {name} ha iniciado el bot!</b>\n\n"
                    "Lista de comandos disponibles:\n\n"
                    "• /ban\n"
                    "Bloquear/Desbloquear usuario"
                    "<blockquote>Bloquea al usuario si no deseas recibir mensajes de él.</blockquote>\n\n"
                    "• /silent\n"
                    "Activar/Desactivar modo silencioso"
                    "<blockquote>Cuando está activado el modo silencioso, los mensajes no se envían al usuario.</blockquote>\n\n"
                    "• /information\n"
                    "Información del usuario"
                    "<blockquote>Recibe un mensaje con información básica sobre el usuario.</blockquote>"
                ),
                "user_restarted_bot": "<b>El usuario {name} ha reiniciado el bot!</b>",
                "user_stopped_bot": "<b>El usuario {name} ha detenido el bot!</b>",
                "user_blocked": "<b>¡Usuario bloqueado!</b> Mensajes del usuario no se aceptan.",
                "user_unblocked": "<b>¡Usuario desbloqueado!</b> Mensajes del usuario se están aceptando nuevamente.",
                "blocked_by_user": "<b>¡Mensaje no enviado!</b> El usuario ha bloqueado al bot.",
                "user_information": (
                    "<b>ID:</b>\n"
                    "- <code>{id}</code>\n"
                    "<b>Nombre:</b>\n"
                    "- {full_name}\n"
                    "<b>Estado:</b>\n"
                    "- {state}\n"
                    "<b>Nombre de usuario:</b>\n"
                    "- {username}\n"
                    "<b>Bloqueado:</b>\n"
                    "- {is_banned}\n"
                    "<b>Fecha de registro:</b>\n"
                    "- {created_at}"
                ),
                "message_not_sent": "<b>¡Mensaje no enviado!</b> Se produjo un error inesperado.",
                "message_sent_to_user": "<b>¡Mensaje enviado al usuario!</b>",
                "silent_mode_enabled": (
                    "<b>¡Modo silencioso activado!</b> Los mensajes no se entregarán al usuario."
                ),
                "silent_mode_disabled": (
                    "<b>¡Modo silencioso desactivado!</b> El usuario recibirá todos los mensajes."
                ),
            },
        }
