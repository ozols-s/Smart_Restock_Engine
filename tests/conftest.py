import pytest
import pandas as pd
from unittest.mock import MagicMock
from datetime import datetime

#sales, analytics
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

#order recommender
@pytest.fixture
def business_params():
    return {
        "lead_time": 2,
        "safety_stock": 10,
        "min_batch": 20
    }

@pytest.fixture
def forecast_df():
    return pd.DataFrame({
        "SKU": ["A", "A", "B", "B"],
        "Value": [10, 20, 30, 40],
        "Date": pd.to_datetime([
            "2024-01-01", "2024-01-02",
            "2024-01-01", "2024-01-02"
        ])
    })

@pytest.fixture
def stock_df():
    return pd.DataFrame({
        "SKU": ["A", "B"],
        "quantity": [5, 10]
    })

@pytest.fixture
def orders_df():
    return pd.DataFrame({
        "SKU": ["A"],
        "quantity": [5]
    })

@pytest.fixture
def empty_orders_df():
    return pd.DataFrame(columns=["SKU", "quantity"])

@pytest.fixture
def empty_stock_df():
    return pd.DataFrame(columns=["SKU", "quantity"])

#order service mocks
@pytest.fixture
def mock_orders_repo(orders_df):
    repo = MagicMock()
    repo.get_orders_in_transit.return_value = orders_df
    return repo

@pytest.fixture
def mock_stock_repo(stock_df):
    repo = MagicMock()
    repo.get_current_stock.return_value = stock_df
    return repo

@pytest.fixture
def mock_forecast_repo(forecast_df):
    repo = MagicMock()
    repo.get_sales_forecast.return_value = forecast_df
    return repo

@pytest.fixture
def order_service(mock_orders_repo, mock_stock_repo, mock_forecast_repo):
    from backend.services.order_service import OrderService

    service = OrderService()
    service.orders_repo = mock_orders_repo
    service.stock_repo = mock_stock_repo
    service.sales_repo = mock_forecast_repo

    return service

#dashboard
@pytest.fixture
def dashboard_sales_df():
    return pd.DataFrame([
        {"product_code": "A", "quantity": 10, "date": "2024-01-01"},
        {"product_code": "A", "quantity": 20, "date": "2024-01-02"},
        {"product_code": "B", "quantity": 5,  "date": "2024-01-01"},
    ])

@pytest.fixture
def dashboard_stock_df():
    return pd.DataFrame([
        {"product_code": "A", "value": 5},
        {"product_code": "B", "value": 10},
    ])

class MockOrder:
    def __init__(self, start, end):
        self.order_date = start
        self.expected_delivery = end

@pytest.fixture
def mock_dashboard_orders():
    return [
        MockOrder(datetime(2024, 1, 1), datetime(2024, 1, 5)),  # 4 дня
        MockOrder(datetime(2024, 1, 1), datetime(2024, 1, 3)),  # 2 дня
    ]

@pytest.fixture
def dashboard_service(
    dashboard_sales_df,
    dashboard_stock_df,
    mock_dashboard_orders
):
    from backend.services.dashboard_service import DashboardService

    service = DashboardService()

    service.sales_repo = MagicMock()
    service.stock_repo = MagicMock()
    service.orders_repo = MagicMock()
    service.order_service = MagicMock()

    service.sales_repo.get_sales.return_value = dashboard_sales_df
    service.stock_repo.get_stock.return_value = dashboard_stock_df
    service.orders_repo.get_all.return_value = mock_dashboard_orders

    service.order_service.calculate_recommended_orders.return_value = [
        {"SKU": "A", "recommended_quantity": 50}
    ]

    return service