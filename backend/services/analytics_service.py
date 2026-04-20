from backend.ml.product_analytics import ProductAnalytics
from backend.repositories.sales_repository import SalesRepository

class AnalyticsService:

    def __init__(self, sales_repository=None):
        self.sales_repo = sales_repository or SalesRepository()

    def _get_sales_df(self):
        return self.sales_repo.get_sales()

    def get_abc(self):
        df = self._get_sales_df()
        analytics = ProductAnalytics(df)

        result = analytics.abc_analysis()

        return result.to_dict(orient="records")

    def get_xyz(self):
        df = self._get_sales_df()
        analytics = ProductAnalytics(df)

        result = analytics.xyz_analysis()

        return result.to_dict(orient="records")

    def get_seasonality(self):
        df = self._get_sales_df()
        analytics = ProductAnalytics(df)

        result = analytics.seasonality_analysis()

        return result.to_dict(orient="records")

    def get_top_products(self):
        df = self._get_sales_df()
        analytics = ProductAnalytics(df)

        result = analytics.top_products_by_profitability()

        return result.to_dict(orient="records")