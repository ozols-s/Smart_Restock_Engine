from flask import Flask
from backend.routes import (
    products_bp,
    orders_bp,
    suppliers_bp
)
from backend.routes.health_route import health_bp
from backend.config.settings import (
    POSTGRES_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS,
    CLICKHOUSE_HOST,
    CLICKHOUSE_PORT,
    CLICKHOUSE_USER,
    CLICKHOUSE_PASSWORD,
    CLICKHOUSE_DB,
    HOST,
    PORT,
    DEBUG
)
from backend.db.connection import init_postgres

def create_app():
    app = Flask(__name__)

    # Настройки SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRES_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

    # Инициализация PostgreSQL через SQLAlchemy
    init_postgres(app)

    # Регистрируем маршруты
    app.register_blueprint(health_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(suppliers_bp)

    return app

# Создаем экземпляр приложения
app = create_app()

if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    )