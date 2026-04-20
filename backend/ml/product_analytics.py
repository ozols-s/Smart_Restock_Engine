import pandas as pd

class ProductAnalytics:

    def __init__(
        self,
        df: pd.DataFrame,
        product_col: str = "product_code",
        revenue_col: str = "revenue",
        quantity_col: str = "quantity",
        date_col: str = "date"
    ):
        self.df = df.copy()

        self.product_col = product_col
        self.revenue_col = revenue_col
        self.quantity_col = quantity_col
        self.date_col = date_col

        # безопасная обработка дат
        if self.date_col in self.df.columns:
            self.df[self.date_col] = pd.to_datetime(
                self.df[self.date_col],
                errors="coerce"
            )

        # убираем мусор
        self.df = self.df.dropna(subset=[self.product_col])

    def abc_analysis(self):

        if self.df.empty:
            return pd.DataFrame()

        revenue = (
            self.df
            .groupby(self.product_col)[self.revenue_col]
            .sum()
            .reset_index()
        )

        revenue = revenue[revenue[self.revenue_col] > 0]

        if revenue.empty:
            return pd.DataFrame()

        revenue = revenue.sort_values(
            by=self.revenue_col,
            ascending=False
        )

        total = revenue[self.revenue_col].sum()

        if total == 0:
            return pd.DataFrame()

        revenue["share"] = revenue[self.revenue_col] / total
        revenue["cumulative"] = revenue["share"].cumsum()

        revenue["category"] = revenue["cumulative"].apply(
            self._assign_abc
        )

        return revenue

    def _assign_abc(self, value: float):

        if value <= 0.8:
            return "A"
        elif value <= 0.95:
            return "B"
        return "C"

    def xyz_analysis(self):

        if self.df.empty or self.date_col not in self.df.columns:
            return pd.DataFrame()

        df = self.df.dropna(subset=[self.date_col]).copy()

        if df.empty:
            return pd.DataFrame()

        df["period"] = df[self.date_col].dt.to_period("M")

        grouped = (
            df
            .groupby([self.product_col, "period"])[self.quantity_col]
            .sum()
            .reset_index()
        )

        result = []

        for product in grouped[self.product_col].unique():

            product_data = grouped[
                grouped[self.product_col] == product
            ][self.quantity_col]

            if len(product_data) < 2:
                continue

            mean = product_data.mean()
            std = product_data.std()

            cv = std / mean if mean > 0 else 0

            result.append({
                self.product_col: product,
                "mean": mean,
                "std": std,
                "cv": cv,
                "xyz_category": self._assign_xyz(cv)
            })

        return pd.DataFrame(result)

    def _assign_xyz(self, cv: float):

        if cv <= 0.1:
            return "X"
        elif cv <= 0.25:
            return "Y"
        return "Z"

    def seasonality_analysis(self):

        if self.df.empty or self.date_col not in self.df.columns:
            return pd.DataFrame()

        df = self.df.dropna(subset=[self.date_col]).copy()

        df["month"] = df[self.date_col].dt.month

        result = (
            df
            .groupby("month")[[self.revenue_col, self.quantity_col]]
            .sum()
            .reset_index()
            .sort_values("month")
        )

        return result

    def top_products_by_profitability(self, top_n: int = 10):

        if self.df.empty:
            return pd.DataFrame()

        grouped = (
            self.df
            .groupby(self.product_col)
            .agg({
                self.revenue_col: "sum",
                self.quantity_col: "sum"
            })
            .reset_index()
        )

        grouped["avg_price"] = grouped[self.revenue_col] / grouped[self.quantity_col].replace(0, 1)

        return grouped.sort_values(
            by=self.revenue_col,
            ascending=False
        ).head(top_n)