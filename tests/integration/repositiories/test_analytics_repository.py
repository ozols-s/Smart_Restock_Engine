from unittest.mock import patch
from backend.repositories.analytics_repository import AnalyticsRepository

@patch("backend.repositories.analytics_repository.get_clickhouse_client")
def test_get_abc_data(mock_client):
    mock_client.return_value.query_df.return_value = [
        ("SKU1", 1000)
    ]

    result = AnalyticsRepository.get_abc_data()

    assert len(result) > 0