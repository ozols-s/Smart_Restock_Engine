import os
from dotenv import load_dotenv

load_dotenv()

#Flask
HOST = "127.0.0.1"
PORT = 5000
DEBUG = True

#PostgreSQL
POSTGRES_URI = os.getenv(
    "POSTGRES_URI",
    "postgresql://postgres:password@localhost:5432/smart_restock"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

#ClickHouse
CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST", "localhost")
CLICKHOUSE_PORT = int(os.getenv("CLICKHOUSE_PORT", 8123))
CLICKHOUSE_USER = os.getenv("CLICKHOUSE_USER", "default")
CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD", "")
CLICKHOUSE_DB = os.getenv("CLICKHOUSE_DB", "default")