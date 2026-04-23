import pandas as pd
import numpy as np


class OrderRecommender:

    def calculate_recommended_order(
        self,
        forecast_df: pd.DataFrame,
        current_stock_df: pd.DataFrame,
        orders_df: pd.DataFrame,
        business_params: dict
    ):

        lead_time = business_params["lead_time"]
        safety_stock = business_params["safety_stock"]
        min_batch = business_params["min_batch"]

        results = []

        for sku in forecast_df["product_code"].unique():

            sku_forecast = forecast_df[forecast_df["product_code"] == sku]
            sku_stock = current_stock_df[current_stock_df["product_code"] == sku]
            sku_orders = orders_df[orders_df["product_code"] == sku]

            current_stock = self._get_current_stock(sku_stock)

            demand = self._calculate_lead_time_demand(
                sku_forecast,
                lead_time
            )

            orders_in_transit = self._calculate_orders_in_transit(
                sku_orders
            )

            required_stock = demand + safety_stock

            available_stock = current_stock + orders_in_transit

            recommended_qty = max(
                0,
                required_stock - available_stock
            )

            if 0 < recommended_qty < min_batch:
                recommended_qty = min_batch

            results.append({
                "SKU": sku,
                "recommended_quantity": float(recommended_qty),
                "current_stock": float(current_stock),
                "orders_in_transit": float(orders_in_transit),
                "demand_during_lead_time": float(demand),
                "safety_stock": float(safety_stock)
            })

        return pd.DataFrame(results)

    def _get_current_stock(self, stock_df):

        if stock_df.empty:
            return 0

        return float(stock_df.iloc[0]["value"])

    def _calculate_lead_time_demand(
        self,
        forecast_df,
        lead_time
    ):

        forecast_df = forecast_df.sort_values("date")

        demand = forecast_df.head(lead_time)["quantity"].sum()

        return float(demand)

    def _calculate_orders_in_transit(self, orders_df):

        if orders_df.empty:
            return 0

        return float(orders_df["quantity"].sum())