import pandas as pd
from backend.ml.product_analytics import ProductAnalytics

#abc_analysis
def test_abc_analysis():
    df = pd.DataFrame([
        {"product_code": "A", "revenue": 100},
        {"product_code": "B", "revenue": 50},
        {"product_code": "C", "revenue": 25},
    ])

    analytics = ProductAnalytics(df)
    result = analytics.abc_analysis()

    assert not result.empty
    assert "category" in result.columns

#xyz_analysis
def test_xyz_analysis():
    df = pd.DataFrame([
        {"product_code": "A", "quantity": 10, "date": "2024-01-01"},
        {"product_code": "A", "quantity": 20, "date": "2024-02-01"},
        {"product_code": "A", "quantity": 15, "date": "2024-03-01"},
    ])

    analytics = ProductAnalytics(df)
    result = analytics.xyz_analysis()

    assert isinstance(result, pd.DataFrame)
    assert "xyz_category" in result.columns

#seasonality
def test_seasonality():
    df = pd.DataFrame([
        {"product_code": "A", "quantity": 10, "date": "2024-01-01", "revenue": 100},
        {"product_code": "A", "quantity": 20, "date": "2024-02-01", "revenue": 200},
    ])

    analytics = ProductAnalytics(df)
    result = analytics.seasonality_analysis()

    assert "month" in result.columns

#top_products
def test_top_products():
    df = pd.DataFrame([
        {"product_code": "A", "revenue": 200, "quantity": 10},
        {"product_code": "B", "revenue": 100, "quantity": 5},
    ])

    analytics = ProductAnalytics(df)
    result = analytics.top_products_by_profitability()

    assert not result.empty
    assert "avg_price" in result.columns