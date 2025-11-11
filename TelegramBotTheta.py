# Основной файл запуска бота
from handlers.message import handle_message
from handlers.models import show_models, set_model
from handlers.clear import clear
from handlers.start import start
from handlers.info import show_info
import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from dotenv import load_dotenv
load_dotenv()  # Загрузка переменных окружения

# Импорт обработчиков команд из разных модулей

# Получение токена из переменных окружения
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Создание экземпляра приложения бота
app = ApplicationBuilder().token(TOKEN).build()

# Регистрация обработчиков команд и сообщений:
app.add_handler(CommandHandler("info", show_info))  # /info
app.add_handler(CommandHandler("start", start))     # /start
app.add_handler(CommandHandler("clear", clear))     # /clear
app.add_handler(CommandHandler("models", show_models))  # /models
app.add_handler(CallbackQueryHandler(set_model))    # Обработка inline-кнопок
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,
                handle_message))  # Обработка текстовых сообщений

# Запуск бота в режиме опроса серверов Telegram
app.run_polling()