import pandas as pd

def test_get_kpi(dashboard_service):
    result = dashboard_service.get_kpi()

    assert "risk_products" in result
    assert "lost_revenue" in result
    assert "avg_lead_time" in result

    assert result["avg_lead_time"] == 3

def test_forecast_graph(dashboard_service):
    result = dashboard_service.get_forecast_graph()

    assert len(result["dates"]) > 0
    assert len(result["sales"]) > 0

def test_forecast_graph_empty(dashboard_service):
    dashboard_service.sales_repo.get_sales.return_value = pd.DataFrame()

    result = dashboard_service.get_forecast_graph()

    assert result["dates"] == []

def test_recommendations(dashboard_service):
    result = dashboard_service.get_recommendations()

    assert isinstance(result, list)
    assert "recommended_quantity" in result[0]

def test_summary(dashboard_service):
    result = dashboard_service.get_summary()

    assert "kpi" in result
    assert "forecast" in result
    assert "recommended_orders" in result