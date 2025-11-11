# Обработчик команды /info
from telegram import Update
from telegram.ext import ContextTypes
from logger import logger


async def show_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Формирование текста со списком команд
    text = (
        "Доступные команды:\n\n"
        "/start — начать работу\n"
        "/models — выбрать модель ИИ\n"
        "/clear — очистить текущую сессию\n"
        "/info — показать данное сообщение\n\n"
    )

    # Логирование запроса
    logger.info(
        f"[{update.message.from_user.id} | @{update.message.from_user.username}] запросил список команд")

    await update.message.reply_text(text)