from flask import Flask

from project.extensions import db
from project.extensions import migrate
# from project.extensions import login_manager  

from project.config import Config



def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    # login_manager.init_app(app)  

    # blueprints will be registered here later
    from project.core.views import core

    app.register_blueprint(core)

    from project import models

    return app