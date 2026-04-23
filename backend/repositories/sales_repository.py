from backend.db.connection import get_clickhouse_client

class SalesRepository:
    def _query_df(self, query: str, parameters: dict = None):
        client = get_clickhouse_client()
        return client.query_df(query, parameters=parameters or {})

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

        return self._query_df(query, {"limit": limit})

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

        return self._query_df(query, {"product_code": product_code})

    def get_sales_aggregated(self):
        query = """
        SELECT 
            product_code,
            sum(quantity) as total_quantity,
            sum(revenue) as total_revenue
        FROM sales_analytics
        GROUP BY product_code
        """

        return self._query_df(query)

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

        return self._query_df(query, {
            "start": start_date,
            "end": end_date
        })