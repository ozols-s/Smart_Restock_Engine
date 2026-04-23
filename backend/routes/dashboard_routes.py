from flask import Blueprint, jsonify

from backend.services import DashboardService


dashboard_service = DashboardService()


dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    url_prefix='/dashboard'
)


@dashboard_bp.route("/recommended", methods=["GET"])
def get_recommended():
    result = dashboard_service.get_recommendations()
    return jsonify({
        "data": result
    })

@dashboard_bp.route("/kpi", methods=["GET"])
def get_kpi():
    result = dashboard_service.get_summary()["kpi"]
    return jsonify({
        "data": result
    })

@dashboard_bp.route("/forecast", methods=["GET"])
def get_forecast():
    result = dashboard_service.get_summary()["forecast"]
    return jsonify({
        "data": result
    })
