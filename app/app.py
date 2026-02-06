from flask import Flask
from config import Config
from extensions import db, jwt, cors
from routes.auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    from .routes.auth import auth_bp
    from .routes.admin import admin_bp
    from .routes.coach import coach_bp
    from .routes.player import player_bp
    from .routes.public import public_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(coach_bp, url_prefix="/api/coach")
    app.register_blueprint(player_bp, url_prefix="/api/player")
    app.register_blueprint(public_bp, url_prefix="/api/public")

    with app.app_context():
        db.create_all()


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
