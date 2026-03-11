'''Файл:

services/analytics_service.py
from backend.ml.product_analytics import ProductAnalytics

class AnalyticsService:

    def get_abc(self, df):
        analytics = ProductAnalytics(df)
        return analytics.abc_analysis()

    def get_xyz(self, df):
        analytics = ProductAnalytics(df)
        return analytics.xyz_analysis()

    def get_seasonality(self, df):
        analytics = ProductAnalytics(df)
        return analytics.seasonality_analysis()

    def get_top_profit(self, df):
        analytics = ProductAnalytics(df)
        return analytics.top_products_by_profitability()'''

"""
Сервис аналитики продаж.

Назначение:
Оркестрация аналитических расчетов.

Что делает сервис:
- получает данные продаж из repositories
- передает DataFrame в ProductAnalytics
- возвращает результат анализа

Основные функции:
- ABC анализ
- XYZ анализ
- сезонность
- прибыльность товаров

Этот слой объединяет:
repositories ↔ аналитические алгоритмы.
"""

from backend.ml.product_analytics import ProductAnalytics
from backend.repositories.clickhouse.sales_repository import SalesRepository


class AnalyticsService:

    def __init__(self):
        self.sales_repo = SalesRepository()

    def abc_analysis(self):

        sales_df = self.sales_repo.get_sales_data()

        analytics = ProductAnalytics(sales_df)

        result = analytics.abc_analysis()

        return result.to_dict(orient="records")

    def xyz_analysis(self):

        sales_df = self.sales_repo.get_sales_data()

        analytics = ProductAnalytics(sales_df)

        result = analytics.xyz_analysis()

        return result.to_dict(orient="records")

    def seasonality_analysis(self, product_id=None):

        sales_df = self.sales_repo.get_sales_data()

        analytics = ProductAnalytics(sales_df)

        result = analytics.seasonality_analysis(product_id)

        return result.to_dict(orient="records")

    def top_products(self):

        sales_df = self.sales_repo.get_sales_data()

        analytics = ProductAnalytics(sales_df)

        result = analytics.top_products_by_profitability()

        return result.to_dict(orient="records")