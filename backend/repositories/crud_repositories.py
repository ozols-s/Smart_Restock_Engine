from backend.db.connection import db
from backend.db.models import Orders, Suppliers, Products

#Orders
class OrdersRepository:
    @staticmethod
    def get_all():
        return Orders.query.all()

    @staticmethod
    def get_by_id(order_id):
        return Orders.query.get(order_id)

    @staticmethod
    def create(**kwargs):
        order = Orders(**kwargs)
        db.session.add(order)
        db.session.commit()
        return order

    @staticmethod
    def update(order_id, **kwargs):
        order = Orders.query.get(order_id)
        if order:
            for key, value in kwargs.items():
                setattr(order, key, value)
            db.session.commit()
        return order

    @staticmethod
    def delete(order_id):
        order = Orders.query.get(order_id)
        if order:
            db.session.delete(order)
            db.session.commit()
        return order

#Suppliers
class SuppliersRepository:
    @staticmethod
    def get_all():
        return Suppliers.query.all()

    @staticmethod
    def get_by_id(supplier_id):
        return Suppliers.query.get(supplier_id)

    @staticmethod
    def create(**kwargs):
        supplier = Suppliers(**kwargs)
        db.session.add(supplier)
        db.session.commit()
        return supplier

    @staticmethod
    def update(supplier_id, **kwargs):
        supplier = Suppliers.query.get(supplier_id)
        if supplier:
            for key, value in kwargs.items():
                setattr(supplier, key, value)
            db.session.commit()
        return supplier

    @staticmethod
    def delete(supplier_id):
        supplier = Suppliers.query.get(supplier_id)
        if supplier:
            db.session.delete(supplier)
            db.session.commit()
        return supplier

#Products
class ProductsRepository:
    @staticmethod
    def get_all():
        return Products.query.all()

    @staticmethod
    def get_by_id(product_id):
        return Products.query.get(product_id)

    @staticmethod
    def create(**kwargs):
        product = Products(**kwargs)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update(product_id, **kwargs):
        product = Products.query.get(product_id)
        if product:
            for key, value in kwargs.items():
                setattr(product, key, value)
            db.session.commit()
        return product

    @staticmethod
    def delete(product_id):
        product = Products.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
        return product