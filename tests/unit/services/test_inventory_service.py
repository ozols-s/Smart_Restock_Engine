import pandas as pd
from unittest.mock import MagicMock

from backend.services.inventory_service import InventoryService

def test_get_sales_df():
    with MagicMock() as mock:
        mock.return_value = [
            ("2024-01-01", "A", 10, 100)
        ]


def test_get_forecast_df(monkeypatch):
    df = pd.DataFrame([
        {"product_code": "A", "quantity": 10, "date": "2024-01-01", "revenue": 100},
        {"product_code": "A", "quantity": 20, "date": "2024-02-01", "revenue": 200},
    ])

    monkeypatch.setattr(
        InventoryService,
        "get_sales_df",
        staticmethod(lambda: df)
    )

    result = InventoryService.get_forecast_df()

    assert not result.empty
    assert "SKU" in result.columns
    assert "Value" in result.columns