from flask import Blueprint, jsonify

from backend.services import SupplierService


supplier_service = SupplierService()


suppliers_bp = Blueprint(
    "suppliers",
    __name__
)


@suppliers_bp.route("/suppliers", methods=["GET"])
def get_all_suppliers():
    suppliers = supplier_service.get_suppliers()
    return jsonify({
        "data": suppliers
    })
