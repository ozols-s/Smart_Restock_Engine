from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from backend.db.connection import db

class Orders(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(50))
    supplier_id = db.Column(db.Integer)
    product_code = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Float)
    total_amount = db.Column(db.Float)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    expected_delivery = db.Column(db.DateTime)
    status = db.Column(db.String(20))
    user_id = db.Column(db.Integer)
    
    def to_dict(self):
        result = {
            "id": self.id,
            "order_number": self.order_number,
            "supplier_id": self.supplier_id,
            "product_code": self.product_code,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "total_amount": self.total_amount,
            "order_date": self.order_date,
            "expected_delivery": self.expected_delivery,
            "status": self.status,
            "user_id": self.user_id
        }
        return result


class Clients(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    client_code = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(200))


class Products(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    is_folder = db.Column(db.Boolean, default=False)
    parent_id = db.Column(db.Integer)
    code = db.Column(db.String(50), unique=True)
    descr = db.Column(db.String(200))
    article = db.Column(db.String(100))
    measure = db.Column(db.String(20))
    nds_rate = db.Column(db.Float)

    def to_dict(self):
        result = {
            "id": self.id,
            "is_folder": self.is_folder,
            "parent_id": self.parent_id,
            "code": self.code,
            "descr": self.descr,
            "article": self.article,
            "measure": self.measure,
            "nds_rate": self.nds_rate
        }
        return result


class Suppliers(db.Model):
    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    contact_person = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    address = db.Column(db.Text)

    def to_dict(self):
        result = {
            "id": self.id,
            "name": self.name,
            "contact_person": self.contact_person,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }
        return result


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(200))
    full_name = db.Column(db.String(150))
    role = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


__all__ = [
    "db",
    "Products",
    "Clients",
    "Orders",
    "Suppliers",
    "Users",
]


"""
Модели базы данных (опционально).

Назначение:
Описание структуры таблиц в виде Python моделей.

Используется только если применяется ORM
например:
- SQLAlchemy ORM
- Pydantic модели
"""