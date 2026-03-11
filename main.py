from flask import Flask
from backend.routes.health_route import health_bp
from backend.config.settings import Settings


def create_app():
    app = Flask(__name__)

    app.config.from_object(Settings)

    # http-routes
    app.register_blueprint(health_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host=Settings.HOST,
        port=Settings.PORT,
        debug=Settings.DEBUG
    )