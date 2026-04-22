CREATE TABLE default.orders_history
(
    id UInt64,
    order_number String,
    supplier_id UInt64,
    product_code String,
    quantity Int32,
    unit_price Float32,
    total_amount Float32,
    order_date DateTime,
    expected_delivery DateTime,
    status String,
    user_id UInt64
)
ENGINE = MergeTree
ORDER BY order_date
SETTINGS index_granularity = 8192;