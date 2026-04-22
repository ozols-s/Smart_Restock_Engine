CREATE TABLE default.stock_levels
(
    product_code String,
    value UInt32,
    date DateTime
)
ENGINE = MergeTree
ORDER BY (product_code, date)
SETTINGS index_granularity = 8192;