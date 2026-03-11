'''Файл:

ml/product_analytics.py

Сюда переносится:

ProductAnalytics

Он содержит:

ABC analysis

XYZ analysis

Seasonality

Profitability

Это логически одна группа → analytics.'''

"""
Модуль аналитики продуктов.

Назначение:
Реализация аналитических алгоритмов для анализа продаж товаров.

Основные функции:
- ABC анализ
- XYZ анализ
- анализ сезонности
- анализ прибыльности товаров

Класс:
ProductAnalytics

Основные методы:
- abc_analysis()
- xyz_analysis()
- seasonality_analysis()
- top_products_by_profitability()

Этот модуль работает только с pandas DataFrame
и не должен содержать:
- SQL
- Flask
- HTTP запросы
- работу с базами данных

Он получает DataFrame и возвращает результаты анализа.
"""

import pandas as pd


class ProductAnalytics:

    def __init__(
        self,
        df,
        product_col="product_code",
        revenue_col="revenue",
        quantity_col="quantity",
        date_col="date"
    ):

        self.df = df.copy()

        self.product_col = product_col
        self.revenue_col = revenue_col
        self.quantity_col = quantity_col
        self.date_col = date_col

        self.df[self.date_col] = pd.to_datetime(
            self.df[self.date_col],
            errors="coerce"
        )

    def abc_analysis(self):

        revenue = (
            self.df
            .groupby(self.product_col)[self.revenue_col]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

        total = revenue[self.revenue_col].sum()

        revenue["share"] = revenue[self.revenue_col] / total

        revenue["cumulative"] = revenue["share"].cumsum()

        revenue["category"] = revenue["cumulative"].apply(
            self._assign_abc
        )

        return revenue

    def _assign_abc(self, value):

        if value <= 0.8:
            return "A"

        if value <= 0.95:
            return "B"

        return "C"

    def xyz_analysis(self):

        df = self.df.copy()

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

            mean = product_data.mean()

            std = product_data.std()

            cv = std / mean if mean > 0 else 0

            category = self._assign_xyz(cv)

            result.append({
                self.product_col: product,
                "cv": cv,
                "xyz_category": category
            })

        return pd.DataFrame(result)

    def _assign_xyz(self, cv):

        if cv <= 0.1:
            return "X"

        if cv <= 0.25:
            return "Y"

        return "Z"