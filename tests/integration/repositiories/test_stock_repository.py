from unittest.mock import patch
from backend.repositories.stock_repository import StockRepository

@patch("backend.repositories.stock_repository.get_clickhouse_client")
def test_get_all_stock(mock_client):
    mock_client.return_value.query_df.return_value = [
        ("SKU1", 10, "2024-01-01")
    ]

    result = StockRepository.get_all()

    assert result is not None