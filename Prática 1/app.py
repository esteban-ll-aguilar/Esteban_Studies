from flask import Flask
def create_app():

    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.config.Config')

    with app.app_context():
        #from routes.api import api
        #app.register_blueprint(api)
        #from routes.listas_version import listas_version
        #app.register_blueprint(listas_version)
        from routes.router import router
        app.register_blueprint(router)
    return app

