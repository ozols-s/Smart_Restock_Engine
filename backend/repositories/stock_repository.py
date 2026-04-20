from backend.db.connection import get_clickhouse_client

class StockRepository:
    @staticmethod
    def get_all():
        client = get_clickhouse_client()

        query = """
        SELECT 
            product_code,
            value,
            date
        FROM stock_levels
        ORDER BY date DESC
        """

        return client.query_df(query)

    @staticmethod
    def get_latest():
        #Получить последние остатки по каждому товару
        client = get_clickhouse_client()

        query = """
        SELECT 
            product_code,
            argMax(value, date) as value
        FROM stock_levels
        GROUP BY product_code
        """

        return client.query_df(query)

    @staticmethod
    def get_by_product(product_code: str):
        client = get_clickhouse_client()

        query = """
        SELECT 
            product_code,
            value,
            date
        FROM stock_levels
        WHERE product_code = %(product_code)s
        ORDER BY date
        """

        return client.query_df(query, parameters={
            "product_code": product_code
        })