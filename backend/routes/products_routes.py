from flask import Blueprint, jsonify

from backend.services import ProductService


product_service = ProductService()


products_bp = Blueprint(
    "products",
    __name__
)


@products_bp.route("/products", methods=["GET"])
def get_all_products():
    products = product_service.get_products()
    return jsonify({
        "data": products
    })
