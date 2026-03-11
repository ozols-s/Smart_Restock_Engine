'''Файл:

services/inventory_service.py

Он вызывает ML.

from backend.ml.order_recommender import OrderRecommender

class InventoryService:

    def __init__(self):
        self.recommender = OrderRecommender()

    def get_recommendations(self, forecast_df, stock_df, orders_df, params):

        result = self.recommender.calculate_recommended_order(
            forecast_df,
            stock_df,
            orders_df,
            params
        )

        return result.to_dict(orient="records")'''

"""
Сервис управления складскими остатками.

Назначение:
Работа с данными о запасах товаров.

Основные задачи:
- получение текущих остатков
- анализ динамики запасов
- подготовка данных для расчета заказов
- интеграция со складскими системами

Источники данных:
- Postgres
- ClickHouse
- внешние системы учета склада
"""

from backend.repositories.postgres.stock_repository import StockRepository


class InventoryService:

    def __init__(self):
        self.stock_repo = StockRepository()

    def get_inventory(self):

        stock_df = self.stock_repo.get_current_stock()

        return stock_df.to_dict(orient="records")

    def get_inventory_by_sku(self, sku: str):

        stock_df = self.stock_repo.get_current_stock()

        result = stock_df[stock_df["SKU"] == sku]

        return result.to_dict(orient="records")