"""
Настройки приложения.

Назначение:
Централизованное хранение всех конфигураций приложения.

Что должно храниться здесь:
- параметры подключения к Postgres
- параметры подключения к ClickHouse
- параметры подключения к Redis
- настройки Flask
- параметры логирования
- переменные окружения

Что должно быть реализовано:
- загрузка переменных из .env
- создание конфигурационных классов или объектов
- доступ к настройкам из любого модуля приложения

Примеры параметров:
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DB
CLICKHOUSE_HOST
REDIS_HOST
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    DEBUG = os.getenv("DEBUG", "True") == "True"

    HOST = os.getenv("HOST", "0.0.0.0")

    PORT = int(os.getenv("PORT", 5000))

    APP_NAME = os.getenv("APP_NAME", "Smart Restock")

    VERSION = os.getenv("VERSION", "1.0.0")