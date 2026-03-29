from flask import Blueprint, jsonify

from backend.services import OrderService


order_service = OrderService()


orders_bp = Blueprint(
    "orders",
    __name__
)


@orders_bp.route("/orders", methods=["GET"])
def get_all_orders():
    orders = order_service.get_orders()
    return jsonify({
        "data": orders
    })
