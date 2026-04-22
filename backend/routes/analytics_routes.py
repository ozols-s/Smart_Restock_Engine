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
