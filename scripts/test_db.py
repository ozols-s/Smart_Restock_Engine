import sys
import os

# Добавляем корень проекта в sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from main import create_app
from backend.db.connection import db
from backend.repositories.crud_repositories import OrdersRepository, ProductsRepository, SuppliersRepository

# Создаем приложение
app = create_app()

# Все операции с db — внутри app context
with app.app_context():
    # получить все заказы
    orders = OrdersRepository.get_all()
    print("Orders:")
    for o in orders:
        print(o.id, o.order_number, o.status)

    # получить все продукты
    products = ProductsRepository.get_all()
    print("\nProducts:")
    for p in products:
        print(p.id, p.code, p.descr)

    # получить всех поставщиков
    suppliers = SuppliersRepository.get_all()
    print("\nSuppliers:")
    for s in suppliers:
        print(s.id, s.name)