import pandas as pd
from unittest.mock import MagicMock, patch

def test_calculate_recommended_orders(order_service, business_params, forecast_df, stock_df, orders_df):
    fixed_date = "2024-01-10"

    sales_df = pd.DataFrame([
        {"product_code": "A", "revenue": 100, "quantity": 10, "date": "2024-01-01"}
    ])

    order_service.sales_repo.get_sales_by_period = MagicMock(return_value=sales_df)
    order_service.forecast_service.forecast_per_product = MagicMock(return_value=forecast_df)
    order_service.stock_repo.get_latest = MagicMock(return_value=stock_df)
    order_service.orders_repo.get_orders_in_transit = MagicMock(return_value=orders_df)

    expected_result = pd.DataFrame([
        {"SKU": "A", "qty": 100}
    ])

    order_service.recommender.calculate_recommended_order = MagicMock(
        return_value=expected_result
    )

    with patch("backend.services.order_service.datetime") as mock_datetime:
        mock_datetime.now.return_value.date.return_value = pd.to_datetime("2024-01-10").date()

        result = order_service.calculate_recommended_orders(business_params)

    # 1. проверяем вызов sales repo
    order_service.sales_repo.get_sales_by_period.assert_called_once()

    # 2. проверяем forecast
    order_service.forecast_service.forecast_per_product.assert_called_once_with(sales_df)

    # 3. проверяем stock
    order_service.stock_repo.get_latest.assert_called_once()

    # 4. проверяем orders
    order_service.orders_repo.get_orders_in_transit.assert_called_once()

    # 5. проверяем recommender вызов
    order_service.recommender.calculate_recommended_order.assert_called_once()

    # 6. проверяем результат
    assert result == expected_result.to_dict(orient="records")