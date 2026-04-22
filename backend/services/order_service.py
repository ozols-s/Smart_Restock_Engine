from datetime import datetime, timedelta

from backend.ml.order_recommender import OrderRecommender

from backend.repositories import OrdersRepository
from backend.repositories.stock_repository import StockRepository
from backend.repositories.sales_repository import SalesRepository

from backend.services.forecast_service import ForecastService

class OrderService:
    def __init__(self):
        self.recommender = OrderRecommender()
        self.orders_repo = OrdersRepository()
        self.stock_repo = StockRepository()
        self.sales_repo = SalesRepository()
        self.forecast_service = ForecastService()

    def get_orders(self):
        raw_orders = self.orders_repo.get_all()
        orders = [order.to_dict() for order in raw_orders]
        return orders

    def calculate_recommended_orders(self, business_params: dict):
        #Период предсказания (последние 7 дней)
        days = business_params.get("forecast_days", 7)
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days)

        sales_df = self.sales_repo.get_sales_by_period(str(start_date), str(end_date))

        forecast_df = self.forecast_service.forecast_per_product(sales_df)
        stock_df = self.stock_repo.get_latest()
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