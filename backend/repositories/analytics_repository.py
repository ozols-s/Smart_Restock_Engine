from backend.db.connection import get_clickhouse_client

class AnalyticsRepository:

    def __init__(self, client=None):
        self.client = client or get_clickhouse_client()

    def get_abc_data(self):
        client = get_clickhouse_client()

        query = """
        SELECT 
            product_code,
            sum(revenue) as revenue
        FROM sales_analytics
        GROUP BY product_code
        ORDER BY revenue DESC
        """

        return self.client.query_df(query)

    def get_xyz_data(self):
        client = get_clickhouse_client()

        query = """
        SELECT 
            product_code,
            toStartOfMonth(date) as period,
            sum(quantity) as quantity
        FROM sales_analytics
        GROUP BY product_code, period
        ORDER BY product_code, period
        """

        return self.client.query_df(query)

    def get_seasonality_data(self):

        query = """
        SELECT 
            toMonth(date) as month,
            sum(revenue) as revenue,
            sum(quantity) as quantity
        FROM sales_analytics
        GROUP BY month
        ORDER BY month
        """

        return self.client.query_df(query)

    def get_top_products(self, limit: int = 10):
        query = """
        SELECT 
            product_code,
            sum(revenue) as revenue,
            sum(quantity) as quantity
        FROM sales_analytics
        GROUP BY product_code
        ORDER BY revenue DESC
        LIMIT %(limit)s
        """

        return self.client.query_df(query, parameters={"limit": limit})