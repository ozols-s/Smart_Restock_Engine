from unittest.mock import MagicMock, patch
import pandas as pd

def test_analytics_service_fully_isolated():
    # 1. mock repository
    mock_repo = MagicMock()

    mock_df = pd.DataFrame([
        {"product_code": "A", "revenue": 100, "quantity": 10},
        {"product_code": "B", "revenue": 200, "quantity": 20},
    ])

    mock_repo.get_sales.return_value = mock_df

    # 2. patch SalesRepository ДО создания сервиса
    with patch(
        "backend.services.analytics_service.SalesRepository",
        return_value=mock_repo
    ):

        from backend.services.analytics_service import AnalyticsService
        service = AnalyticsService()

        # 3. patch ProductAnalytics
        with patch(
            "backend.services.analytics_service.ProductAnalytics"
        ) as MockAnalytics:

            instance = MockAnalytics.return_value

            # мокируем методы аналитики
            instance.abc_analysis.return_value = pd.DataFrame([
                {"product_code": "A"}
            ])

            instance.xyz_analysis.return_value = pd.DataFrame([
                {"product_code": "B"}
            ])

            instance.seasonality_analysis.return_value = pd.DataFrame([
                {"month": 1}
            ])

            instance.top_products_by_profitability.return_value = pd.DataFrame([
                {"product_code": "A"}
            ])

            # 4. вызовы сервиса
            abc = service.get_abc()
            xyz = service.get_xyz()
            season = service.get_seasonality()
            top = service.get_top_products()

            # 5. проверки результата
            assert isinstance(abc, list)
            assert isinstance(xyz, list)
            assert isinstance(season, list)
            assert isinstance(top, list)

            assert abc == [{"product_code": "A"}]
            assert xyz == [{"product_code": "B"}]

            # 6. проверки изоляции
            mock_repo.get_sales.assert_called_once()

            assert MockAnalytics.call_count == 1