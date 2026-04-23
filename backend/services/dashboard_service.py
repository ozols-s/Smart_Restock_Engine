import pandas as pd
import random

from backend.repositories.sales_repository import SalesRepository
from backend.repositories.stock_repository import StockRepository
from backend.repositories.crud_repositories import OrdersRepository

from backend.services.order_service import OrderService

from backend.config.business_params import BUSINESS_PARAMS

from backend.cache.cache_decorator import cache


class DashboardService:
    def __init__(self):
        self.sales_repo = SalesRepository()
        self.stock_repo = StockRepository()
        self.orders_repo = OrdersRepository()

        self.order_service = OrderService()

    #KPI
    def get_kpi(self):
        sales_df = self.sales_repo.get_sales()
        stock_df = self.stock_repo.get_latest()

        risk_products = self._calculate_risk_products(sales_df, stock_df)
        forecast_accuracy = random.uniform(0.93, 0.96) #пока заглушка
        lost_revenue = self._calculate_lost_revenue(sales_df, stock_df)
        avg_lead_time = self._calculate_lead_time()

        return {
            "risk_products": risk_products,
            "forecast_accuracy": forecast_accuracy,
            "lost_revenue": lost_revenue,
            "avg_lead_time": avg_lead_time
        }

    #График
    def get_forecast_graph(self, product_code=None):
        sales_df = self.sales_repo.get_sales()

        if product_code:
            sales_df = sales_df[sales_df["product_code"] == product_code]

        if sales_df.empty:
            return {
                "dates": [],
                "sales": [],
                "forecast": [],
                "stock": []
            }

        sales_df["date"] = pd.to_datetime(sales_df["date"])
        sales_df = sales_df.sort_values("date")

        grouped = sales_df.groupby("date")["quantity"].sum().reset_index()

        grouped["forecast"] = (
            grouped["quantity"]
            .rolling(3)
            .mean()
            .bfill()
        )
        grouped["stock"] = grouped["quantity"].iloc[::-1].cumsum().iloc[::-1]

        return {
            "dates": grouped["date"].astype(str).tolist(),
            "sales": grouped["quantity"].tolist(),
            "forecast": grouped["forecast"].tolist(),
            "stock": grouped["stock"].tolist()
        }

    #Рекомендуемый заказ
    def get_recommendations(self):
        params = BUSINESS_PARAMS
        return self.order_service.calculate_recommended_orders(params)

    @cache(ttl=120)
    def get_summary(self):
        return {
            "kpi": self.get_kpi(),
            "forecast": self.get_forecast_graph(),
            "recommended_orders": self.get_recommendations()
        }

    #Вспомогательные
    def _calculate_risk_products(self, sales_df, stock_df):
        if sales_df.empty or stock_df.empty:
            return 0

        sales_sum = sales_df.groupby("product_code")["quantity"].sum()
        stock_sum = stock_df.groupby("product_code")["value"].sum()

        merged = pd.concat([sales_sum, stock_sum], axis=1).fillna(0)
        merged.columns = ["sales", "stock"]

        risk = merged[merged["stock"] < merged["sales"]]

        return int(len(risk))

    def _calculate_lost_revenue(self, sales_df, stock_df):
        if sales_df.empty or stock_df.empty:
            return 0

        avg_price = 100

        sales_sum = sales_df.groupby("product_code")["quantity"].sum()
        stock_sum = stock_df.groupby("product_code")["value"].sum()

        merged = pd.concat([sales_sum, stock_sum], axis=1).fillna(0)
        merged.columns = ["sales", "stock"]

        lost = merged[merged["stock"] < merged["sales"]]
        lost_qty = (lost["sales"] - lost["stock"]).clip(lower=0).sum()

        return float(lost_qty * avg_price)

    def _calculate_lead_time(self):
        orders = self.orders_repo.get_all()

        if not orders:
            return 0

        durations = [
            (o.expected_delivery - o.order_date).days
            for o in orders
            if o.order_date and o.expected_delivery
        ]

        if not durations:
            return 0

        return round(sum(durations) / len(durations), 2)