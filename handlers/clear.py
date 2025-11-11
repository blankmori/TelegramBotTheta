# Обработчик команды /clear
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from logger import logger


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    context.user_data.clear()  # Очистка пользовательских данных

    # Логирование действия
    logger.info(
        f"[{user.id} | @{user.username}] завершил сессию и очистил память (/clear)")

    # Отправка подтверждения с удалением клавиатуры
    await update.message.reply_text(
        "Сессия завершена. Память очищена.",
        reply_markup=ReplyKeyboardRemove()
    )