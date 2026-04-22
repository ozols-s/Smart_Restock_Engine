import pandas as pd

class ForecastService:
    def __init__(self, window=3):
        self.window = window

    def simple_moving_average(self, df, window=3):
        df = df.sort_values("date")

        df["forecast"] = (
            df["quantity"]
            .rolling(self.window)
            .mean()
            .bfill()
        )

        return df

    def forecast_per_product(self, df):
        if df.empty:
            return pd.DataFrame()

        df["date"] = pd.to_datetime(df["date"])

        result = []

        for product in df["product_code"].unique():

            product_df = df[df["product_code"] == product]

            grouped = (
                product_df
                .groupby("date")["quantity"]
                .sum()
                .reset_index()
            )

            forecast_df = self.simple_moving_average(grouped)

            forecast_df["product_code"] = product

            result.append(forecast_df)

        return pd.concat(result)