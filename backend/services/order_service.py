"""
Сервис управления заказами.

Назначение:
Оркестрация логики расчета рекомендованных заказов.

Что делает сервис:
1. Получает данные из repositories
2. Подготавливает DataFrame
3. передает данные в OrderRecommender
4. возвращает результат API

Основные шаги:
- загрузка прогноза продаж
- загрузка текущих остатков
- загрузка заказов в пути
- запуск алгоритма расчета заказа

Этот слой НЕ содержит:
- SQL
- аналитические алгоритмы

Он только связывает:
repositories ↔ ml модули.
"""


from backend.ml.order_recommender import OrderRecommender
from backend.repositories import OrdersRepository
# from backend.repositories.stock_repository import StockRepository
# from backend.repositories.sales_repository import SalesRepository

class OrderService:
    def __init__(self):
        self.recommender = OrderRecommender()
        self.orders_repo = OrdersRepository()
        # self.stock_repo = StockRepository()
        # self.sales_repo = SalesRepository()

    def get_orders(self):
        raw_orders = self.orders_repo.get_all()
        orders = [order.to_dict() for order in raw_orders]
        return orders

    def calculate_recommended_orders(self, business_params: dict):
        forecast_df = self.sales_repo.get_sales_forecast()
        stock_df = self.stock_repo.get_current_stock()
        orders_df = self.orders_repo.get_orders_in_transit()
        result = self.recommender.calculate_recommended_order(
            forecast_df,
            stock_df,
            orders_df,
            business_params
        )
        return result.to_dict(orient="records")


class ManualOrderService:
    @staticmethod
    def create_order(data):
        if data["quantity"] <= 0:
            raise ValueError("Quantity must be positive")

        return OrdersRepository.create(data)