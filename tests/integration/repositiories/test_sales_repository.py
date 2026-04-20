from unittest.mock import MagicMock, patch
from backend.repositories.sales_repository import SalesRepository

@patch("backend.repositories.sales_repository.get_clickhouse_client")
def test_get_sales(mock_client):
    mock_client.return_value.query_df.return_value = [
        ("SKU1", "2024-01-01", 10, 100)
    ]

    result = SalesRepository.get_sales()

    assert result is not None
    mock_client.return_value.query_df.assert_called_once()