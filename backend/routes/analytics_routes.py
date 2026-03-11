'''Файл:

routes/analytics_routes.py
from flask import Blueprint
from backend.services.analytics_service import AnalyticsService

analytics_bp = Blueprint("analytics", __name__)
service = AnalyticsService()

@analytics_bp.route("/abc")
def abc():
    return service.get_abc(...)'''

"""
HTTP маршруты Flask API.

Назначение:
Определение REST API эндпоинтов.

Каждый маршрут:
- принимает HTTP запрос
- валидирует параметры
- вызывает соответствующий сервис
- возвращает JSON ответ

Routes НЕ должны содержать:
- бизнес логику
- SQL
- аналитические алгоритмы

Они только вызывают сервисы.
"""