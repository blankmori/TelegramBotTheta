# Обработчик текстовых сообщений
from telegram import Update
from telegram.ext import ContextTypes
from services.io_api import send_to_io_api
from logger import logger

DEFAULT_MODEL = "openchat/openchat-3.5-0106"  # Модель по умолчанию


def parse_ai_response(full_text: str) -> str:
    # Очистка ответа модели от служебных маркеров
    if "</think>" in full_text:
        return full_text.split("</think>", 1)[1].strip()
    return full_text.strip()


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    model = context.user_data.get("model", DEFAULT_MODEL)

    # Логирование входящего сообщения
    logger.info(f"[{user.id} | @{user.username}] → {update.message.text}")

    # Подготовка истории чата (последние 5 сообщений)
    chat_history = context.user_data.get("chat_history", [])
    chat_history.append(f"Пользователь: {update.message.text}")
    prompt = "\n".join(chat_history)

    # Получение и обработка ответа от модели
    full_reply = send_to_io_api(prompt, model)
    clean_reply = parse_ai_response(full_reply)

    # Сохранение истории
    chat_history.append(f"Бот: {clean_reply}")
    # Ограничение истории
    context.user_data["chat_history"] = chat_history[-5:]

    # Логирование и отправка ответа
    logger.info(f"[{user.id} | @{user.username}] ← {clean_reply[:100]}...")
    await update.message.reply_text(clean_reply)