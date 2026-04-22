from flask import Blueprint, jsonify

from backend.services import AnalyticsService


analytics_service = AnalyticsService()


analytics_bp = Blueprint(
    "analytics",
    __name__,
    url_prefix='/analytics'
)


@analytics_bp.route("/abc", methods=["GET"])
def get_analytics_abc():
    result = analytics_service.get_abc()
    return jsonify({
        "data": result
    })

@analytics_bp.route("/xyz", methods=["GET"])
def get_analytics_xyz():
    result = analytics_service.get_xyz()
    return jsonify({
        "data": result
    })

@analytics_bp.route("/seasonality", methods=["GET"])
def get_analytics_seasonality():
    result = analytics_service.get_seasonality()
    return jsonify({
        "data": result
    })

@analytics_bp.route("/top-products", methods=["GET"])
def get_analytics_top_products():
    result = analytics_service.get_top_products()
    return jsonify({
        "data": result
    })
