# Обработчик команды /start
from telegram import Update
from telegram.ext import ContextTypes
from logger import logger


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Логирование нового пользователя
    logger.info(
        f"[{update.message.from_user.id} | @{update.message.from_user.username}] использовал /start")

    await update.message.reply_text(
        "Бот активен. Для ознакомления с командами используйте: /info."
    )