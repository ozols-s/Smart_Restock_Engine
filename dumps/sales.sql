CREATE TABLE default.sales
(
    id UInt64,
    product_code String,
    client_code String,
    earned Float32,
    value Int32,
    date DateTime
)
ENGINE = MergeTree
ORDER BY date
SETTINGS index_granularity = 8192;