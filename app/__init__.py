from flask import Flask
from app.extensions import db, bcrypt, login_manager, migrate

from app.main.routes import main_bp
from app.auth.routes import auth_bp
from app.artwork.routes import artwork_bp
from app.cart.routes import cart_bp
from app.order.routes import order_bp
from app.profile.routes import profile_bp

import os

from app.models import User, Artwork, CartItem, Order, OrderItem


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
    app.secret_key = os.environ.get("SECRET_KEY")

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please login before access this page!"
    login_manager.login_message_category = "warning"

    app.register_blueprint(main_bp, url_prefix="/")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(profile_bp, url_prefix="/profile")
    app.register_blueprint(artwork_bp, url_prefix="/artwork")
    app.register_blueprint(cart_bp, url_prefix="/cart")
    app.register_blueprint(order_bp, url_prefix="/order")

    return app