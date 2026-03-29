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

from backend.repositories import SuppliersRepository


class SupplierService:

    def __init__(self):
        self.supplier_repo = SuppliersRepository()

    def get_suppliers(self):
        raw_suppliers = self.supplier_repo.get_all()
        suppliers = [supplier.to_dict() for supplier in raw_suppliers]
        return suppliers
