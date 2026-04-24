from flask import Blueprint, jsonify, render_template

from backend.services import OrderService

order_service = OrderService()

orders_bp = Blueprint(
    "orders",
    __name__
)

@orders_bp.route("/api/orders", methods=["GET"])
def get_all_orders():
    orders = order_service.get_orders()
    return jsonify({
        "data": orders
    })

@orders_bp.route("/orders", methods=["GET"])
def orders():
   return render_template("orders.html")