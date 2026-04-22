from backend.routes.products_routes import products_bp
from backend.routes.orders_routes import orders_bp
from backend.routes.suppliers_routes import suppliers_bp
from backend.routes.analytics_routes import analytics_bp


__all__ = [
    "products_bp",
    "orders_bp",
    "suppliers_bp"
]