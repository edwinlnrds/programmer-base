from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized

db = SQLAlchemy()


def create_app():
    from flask import Flask
    app = Flask(__name__, static_folder='public',
                static_url_path='/public', template_folder='views')
    from app.config import Config
    app.config.from_object(Config)

    db.init_app(app)

    from flask_login import LoginManager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from app.models.Post import Post
    from app.models.Reply import Reply
    from app.models.User import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    from flask_session import Session
    session = Session()
    session.init_app(app)

    from app.routes.base import base
    app.register_blueprint(base)

    from app.routes.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from app.routes.profile import profile
    app.register_blueprint(profile, url_prefix='/u')

    from app.routes.forum import forum
    app.register_blueprint(forum, url_prefix='/posts')

    from app.error_handler import handle_error
    app.register_error_handler(BadRequest, handle_error)
    app.register_error_handler(Unauthorized, handle_error)
    app.register_error_handler(NotFound, handle_error)

    return app
