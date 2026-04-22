from backend.db.connection import get_clickhouse_client

client = get_clickhouse_client()

query = """
CREATE VIEW IF NOT EXISTS sales_analytics AS
SELECT
    product_code,
    date,
    value AS quantity,
    earned AS revenue
FROM sales
"""

client.command(query)

print("VIEW sales_analytics создан")