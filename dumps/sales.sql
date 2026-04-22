CREATE TABLE default.sales_analytics
(
    id UInt64,
    product_code String,
    client_code String,
    revenue Float32,
    quantity Int32,
    date DateTime
)
ENGINE = MergeTree
ORDER BY date
SETTINGS index_granularity = 8192;