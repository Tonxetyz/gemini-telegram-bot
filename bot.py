import logging
import os

import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")

WELCOME_TEXT = (
    "Привет! 👋 Я бот с искусственным интеллектом на базе Gemini.\n\n"
    "Просто напишите мне любое сообщение, и я отвечу с помощью нейросети."
)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY", ""))
model = genai.GenerativeModel(
    GEMINI_MODEL,
    system_instruction="Ты полезный ассистент. Всегда отвечай на русском языке.",
)


async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(WELCOME_TEXT)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        response = await model.generate_content_async(update.message.text)
        await update.message.reply_text(response.text)
    except Exception:
        logger.exception("Gemini request failed")
        await update.message.reply_text(
            "Извините, произошла ошибка при обращении к нейросети. Попробуйте ещё раз чуть позже."
        )


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.exception("Unhandled error", exc_info=context.error)


def main() -> None:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", handle_start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(on_error)
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
