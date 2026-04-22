from backend.ml.order_recommender import OrderRecommender
import pandas as pd

def test_basic_recommendation(forecast_df, stock_df, orders_df, business_params):
    recommender = OrderRecommender()

    result = recommender.calculate_recommended_order(
        forecast_df,
        stock_df,
        orders_df,
        business_params
    )

    assert not result.empty
    assert "recommended_quantity" in result.columns


def test_min_batch_applied(forecast_df, stock_df, empty_orders_df, business_params):
    recommender = OrderRecommender()

    result = recommender.calculate_recommended_order(
        forecast_df.head(1),  # уменьшаем спрос
        stock_df,
        pd.DataFrame(columns=["SKU", "quantity"]),
        business_params
    )

    row = result.iloc[0]

    assert row["recommended_quantity"] >= business_params["min_batch"]


def test_zero_recommendation(forecast_df, business_params):
    recommender = OrderRecommender()

    big_stock = forecast_df.copy()
    big_stock = big_stock[["SKU"]].drop_duplicates()
    big_stock["quantity"] = 1000

    result = recommender.calculate_recommended_order(
        forecast_df,
        big_stock,
        pd.DataFrame(columns=["SKU", "quantity"]),
        business_params=business_params
    )

    assert (result["recommended_quantity"] == 0).all()