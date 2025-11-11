# Управление выбором моделей ИИ
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from services.io_api import fetch_available_models
from logger import logger


async def show_models(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Отображение списка моделей в виде inline-клавиатуры
    models = fetch_available_models()

    # Создание кнопок для каждой модели
    keyboard = [[InlineKeyboardButton(
        model, callback_data=model)] for model in models]

    await update.message.reply_text(
        "Выберите модель:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def set_model(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Обработка выбора модели из inline-клавиатуры
    query = update.callback_query
    context.user_data["model"] = query.data  # Сохранение выбора

    # Подтверждение выбора и логирование
    logger.info(
        f"[{query.from_user.id} | @{query.from_user.username}] выбрал модель {query.data}")
    await query.edit_message_text(f"Модель установлена: {query.data}")