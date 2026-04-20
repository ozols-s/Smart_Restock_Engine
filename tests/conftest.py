import pytest
import pandas as pd
from unittest.mock import MagicMock

@pytest.fixture
def sales_df():
    return pd.DataFrame([
        {"product_code": "A", "revenue": 100, "quantity": 10, "date": "2024-01-01"},
        {"product_code": "A", "revenue": 200, "quantity": 20, "date": "2024-02-01"},
        {"product_code": "B", "revenue": 50,  "quantity": 5,  "date": "2024-01-01"},
        {"product_code": "B", "revenue": 60,  "quantity": 6,  "date": "2024-02-01"},
        {"product_code": "C", "revenue": 25,  "quantity": 2,  "date": "2024-01-01"},
    ])


@pytest.fixture
def mock_sales_repo(sales_df):
    repo = MagicMock()
    repo.get_sales.return_value = sales_df
    return repo


@pytest.fixture
def analytics_service(mock_sales_repo):
    from backend.services.analytics_service import AnalyticsService

    service = AnalyticsService()
    service.sales_repo = mock_sales_repo
    return service