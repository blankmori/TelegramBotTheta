# Конфигурация системы логирования
import logging

# Настройка базовой конфигурации логирования
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования INFO и выше
    format="%(asctime)s - %(levelname)s - %(message)s",  # Формат записи логов
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),  # Запись в файл
        logging.StreamHandler()  # Вывод в консоль
    ]
)

# Создание основного логгера для приложения
logger = logging.getLogger(__name__)