#Собирает данные для подсчета необходимого заказа
import pandas as pd

from backend.repositories.sales_repository import SalesRepository
from backend.repositories.crud_repositories import OrdersRepository, ProductsRepository
from backend.repositories.stock_repository import StockRepository

class InventoryService:

    @staticmethod
    def get_sales_df():
        data = SalesRepository.get_sales()

        if not data:
            return pd.DataFrame()

        df = pd.DataFrame(data, columns=["date", "product_code", "quantity", "revenue"])
        return df

    @staticmethod
    def get_stock_df():
        stocks = StockRepository.get_all()

        return pd.DataFrame([
            {
                "SKU": s.product_code,
                "stock": s.value
            }
            for s in stocks
        ])

    @staticmethod
    def get_orders_df():
        orders = OrdersRepository.get_all()

        return pd.DataFrame([
            {
                "SKU": o.product_code,
                "quantity": o.quantity,
                "expected_delivery": o.expected_delivery,
                "status": o.status
            }
            for o in orders
        ])

    @staticmethod
    def get_forecast_df():
        #позже сюда будет подключено ml
        sales_df = InventoryService.get_sales_df()

        if sales_df.empty:
            return pd.DataFrame()

        # простейший forecast = среднее
        forecast = (
            sales_df.groupby("product_code")["quantity"]
            .mean()
            .reset_index()
        )

        forecast.rename(columns={
            "product_code": "SKU",
            "quantity": "Value"
        }, inplace=True)

        forecast["Date"] = pd.Timestamp.now()

        return forecast