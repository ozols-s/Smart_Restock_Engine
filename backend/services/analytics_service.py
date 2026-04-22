from backend.ml.product_analytics import ProductAnalytics
from backend.repositories.sales_repository import SalesRepository

class AnalyticsService:
    def __init__(self, sales_repository=None):
        self.sales_repo = sales_repository or SalesRepository()

        self._df = None
        self._analytics = None

    #Сделал один вызов в БД вместо 4х
    def _get_df(self):
        if self._df is None:
            self._df = self.sales_repo.get_sales()
        return self._df

    #Один вызов класса вместо 4х
    def _get_analytics(self):
        if self._analytics is None:
            self._analytics = ProductAnalytics(self._get_df())
        return self._analytics

    def get_abc(self):
        return self._get_analytics().abc_analysis().to_dict("records")

    def get_xyz(self):
        return self._get_analytics().xyz_analysis().to_dict("records")

    def get_seasonality(self):
        return self._get_analytics().seasonality_analysis().to_dict("records")

    def get_top_products(self):
        return self._get_analytics().top_products_by_profitability().to_dict("records")