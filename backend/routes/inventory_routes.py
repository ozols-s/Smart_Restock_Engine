'''Файл:

routes/inventory_routes.py
from flask import Blueprint
from backend.services.inventory_service import InventoryService

inventory_bp = Blueprint("inventory", __name__)
service = InventoryService()

@inventory_bp.route("/recommendation")
def recommendation():

    result = service.get_recommendations(...)

    return result'''