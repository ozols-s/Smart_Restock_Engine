from flask import Blueprint, jsonify, render_template

from backend.services import ProductService


product_service = ProductService()


products_bp = Blueprint(
    "products",
    __name__
)


@products_bp.route("/api/products", methods=["GET"])
def get_all_products():
    products = product_service.get_products()
    return jsonify({
        "data": products
    })

@products_bp.route("/products", methods=["GET"])
def products():
   return render_template("products.html")