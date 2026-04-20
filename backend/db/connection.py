from flask_sqlalchemy import SQLAlchemy
import clickhouse_connect
from backend.config.settings import (
    POSTGRES_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS,
    CLICKHOUSE_HOST,
    CLICKHOUSE_PORT,
    CLICKHOUSE_USER,
    CLICKHOUSE_PASSWORD,
    CLICKHOUSE_DB
)

#PostgreSQL
db = SQLAlchemy()

def init_postgres(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRES_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)

#ClickHouse
_client = None

def get_clickhouse_client():
    global _client
    if _client is None:
        _client = clickhouse_connect.get_client(
            host=CLICKHOUSE_HOST,
            port=CLICKHOUSE_PORT,
            username=CLICKHOUSE_USER,
            password=CLICKHOUSE_PASSWORD,
            database=CLICKHOUSE_DB
        )
    return _client