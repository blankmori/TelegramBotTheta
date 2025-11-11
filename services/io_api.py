# Модуль для работы с API Intelligence.io
import requests
import os
from dotenv import load_dotenv
load_dotenv()

IOINTELLIGENCE_API_KEY = os.getenv(
    "IOINTELLIGENCE_API_KEY")  # API-ключ из окружения
print(IOINTELLIGENCE_API_KEY)

def fetch_available_models():
    # Получение списка доступных моделей из API
    url = "https://api.intelligence.io.solutions/api/v1/models"
    headers = {"Authorization": f"Bearer {IOINTELLIGENCE_API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        return [m["id"] for m in response.json().get("data", [])]
    except Exception as e:
        print(f"[ERROR] Не удалось получить модели: {e}")
        return []  # Возвращаем пустой список при ошибке


def send_to_io_api(message: str, model: str) -> str:
    # Отправка сообщения в API и получение ответа модели
    url = "https://api.intelligence.io.solutions/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {IOINTELLIGENCE_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": message}]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[ERROR] Ошибка при обращении к API: {e}")
        return "Ошибка при получении ответа от модели."