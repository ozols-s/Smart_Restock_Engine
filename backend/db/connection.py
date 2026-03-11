import os

from flask_sqlalchemy import SQLAlchemy
import clickhouse_connect
import redis

# PostgreSQL
db = SQLAlchemy()

def init_postgres(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "POSTGRES_URI",
        "postgresql://postgres:password@localhost:5432/smart_restock"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

# ClickHouse
def get_clickhouse_client():
    client = clickhouse_connect.get_client(
        host=os.getenv("CLICKHOUSE_HOST", "localhost"),
        port=int(os.getenv("CLICKHOUSE_PORT", 8123)),
        username=os.getenv("CLICKHOUSE_USER", "default"),
        password=os.getenv("CLICKHOUSE_PASSWORD", ""),
        database=os.getenv("CLICKHOUSE_DB", "default")
    )

    return client

# Redis
def get_redis_client():
    return redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        db=0,
        decode_responses=True
    )

"""
Подключения к базам данных.

Назначение:
Создание и управление подключениями к:
- Postgres
- ClickHouse

Что должно быть реализовано:

Postgres:
- создание SQLAlchemy engine
- функция получения соединения

ClickHouse:
- создание клиента clickhouse-connect
- функция получения клиента

Этот файл НЕ должен содержать SQL запросы.

Он отвечает только за:
- инициализацию соединений
- переиспользование соединений
"""