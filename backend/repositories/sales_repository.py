from backend.db.connection import get_clickhouse_client

class SalesRepository:

    def __init__(self, client=None):
        self.client = client or get_clickhouse_client()

    def get_sales(self, limit: int = 10000):
        query = """
        SELECT 
            product_code,
            date,
            quantity,
            revenue
        FROM sales_analytics
        ORDER BY date DESC
        LIMIT %(limit)s
        """

        return self.client.query_df(query, parameters={"limit": limit})

    def get_sales_by_product(self, product_code: str):
        query = """
        SELECT 
            product_code,
            date,
            quantity,
            revenue
        FROM sales_analytics
        WHERE product_code = %(product_code)s
        ORDER BY date
        """

        return self.client.query_df(query, parameters={"product_code": product_code})

    def get_sales_aggregated(self):
        query = """
        SELECT 
            product_code,
            sum(quantity) as total_quantity,
            sum(revenue) as total_revenue
        FROM sales_analytics
        GROUP BY product_code
        """

        return self.client.query_df(query)

    def get_sales_by_period(self, start_date: str, end_date: str):
        query = """
        SELECT 
            product_code,
            date,
            quantity,
            revenue
        FROM sales_analytics
        WHERE date BETWEEN %(start)s AND %(end)s
        """

        return self.client.query_df(query, parameters={
            "start": start_date,
            "end": end_date
        })