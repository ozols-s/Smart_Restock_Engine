from backend.db.connection import get_clickhouse_client

class AnalyticsRepository:

    @staticmethod
    def get_abc_data():
        client = get_clickhouse_client()

        query = """
        SELECT 
            product_code,
            sum(revenue) as revenue
        FROM sales
        GROUP BY product_code
        ORDER BY revenue DESC
        """

        return client.query_df(query)

    @staticmethod
    def get_xyz_data():
        client = get_clickhouse_client()

        query = """
        SELECT 
            product_code,
            toStartOfMonth(date) as period,
            sum(quantity) as quantity
        FROM sales
        GROUP BY product_code, period
        ORDER BY product_code, period
        """

        return client.query_df(query)

    @staticmethod
    def get_seasonality_data():
        client = get_clickhouse_client()

        query = """
        SELECT 
            toMonth(date) as month,
            sum(revenue) as revenue,
            sum(quantity) as quantity
        FROM sales
        GROUP BY month
        ORDER BY month
        """

        return client.query_df(query)

    @staticmethod
    def get_top_products(limit: int = 10):
        client = get_clickhouse_client()

        query = """
        SELECT 
            product_code,
            sum(revenue) as revenue,
            sum(quantity) as quantity
        FROM sales
        GROUP BY product_code
        ORDER BY revenue DESC
        LIMIT %(limit)s
        """

        return client.query_df(query, parameters={"limit": limit})