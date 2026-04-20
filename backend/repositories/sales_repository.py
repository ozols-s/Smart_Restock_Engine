from backend.db.connection import get_clickhouse_client

class SalesRepository:

    @staticmethod
    def get_sales(limit: int = 10000):
        client = get_clickhouse_client()

        query = """
        SELECT 
            product_code,
            date,
            quantity,
            revenue
        FROM sales
        ORDER BY date DESC
        LIMIT %(limit)s
        """

        return client.query_df(query, parameters={"limit": limit})

    @staticmethod
    def get_sales_by_product(product_code: str):
        client = get_clickhouse_client()

        query = """
        SELECT 
            product_code,
            date,
            quantity,
            revenue
        FROM sales
        WHERE product_code = %(product_code)s
        ORDER BY date
        """

        return client.query_df(query, parameters={"product_code": product_code})

    @staticmethod
    def get_sales_aggregated():
        client = get_clickhouse_client()

        query = """
        SELECT 
            product_code,
            sum(quantity) as total_quantity,
            sum(revenue) as total_revenue
        FROM sales
        GROUP BY product_code
        """

        return client.query_df(query)

    @staticmethod
    def get_sales_by_period(start_date: str, end_date: str):
        client = get_clickhouse_client()

        query = """
        SELECT 
            product_code,
            date,
            quantity,
            revenue
        FROM sales
        WHERE date BETWEEN %(start)s AND %(end)s
        """

        return client.query_df(query, parameters={
            "start": start_date,
            "end": end_date
        })