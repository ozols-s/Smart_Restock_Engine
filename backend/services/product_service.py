"""
Сервис работы с товарами.

Назначение:
Бизнес логика работы с продуктами.

Примеры задач:
- получение списка товаров
- получение статистики по SKU
- фильтрация товаров
- агрегирование данных по продуктам

Сервис получает данные из repositories
и подготавливает их для API.
"""

from backend.repositories.postgres.product_repository import ProductRepository


class ProductService:

    def __init__(self):
        self.product_repo = ProductRepository()

    def get_products(self):

        df = self.product_repo.get_products()

        return df.to_dict(orient="records")

    def get_product(self, product_code: str):

        df = self.product_repo.get_product(product_code)

        return df.to_dict(orient="records")