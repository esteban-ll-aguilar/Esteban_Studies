from flask import Flask
def create_app():

    app = Flask(__name__, instance_relative_config=False)
    app.secret_key = 'clave_secreta'

    app.config.from_object('config.config.Config')

    with app.app_context():
        #from routes.api import api
        #app.register_blueprint(api)
        """ from routes.array_version import array_version
        app.register_blueprint(array_version) """
        from routes.router import router
        app.register_blueprint(router)
    return app

