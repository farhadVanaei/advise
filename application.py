from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from extensions import *

class advisor():
    DEFAULT_APP_NAME = 'project'

    def __init__(self,config = None, app_name=None):
        if app_name is None :
            app_name = advisor.DEFAULT_APP_NAME
        self.db = SQLAlchemy()
        self.login_manager = LoginManager()
        self.app = Flask(app_name, static_folder='media/statics', template_folder='media/templates')
        self.config = config
        self.configure_app()
        self.configure_blueprints()
        self.configure_extentions()

    def configure_app(self):
        if self.config is not None:
            self.app.config.from_object(self.config)
        self.app.config.from_envvar('project_CONFIG', silent=True)

    def configure_blueprints(self):
        self.app.config.setdefault('INSTALLED_BLUEPRINTS', [])
        blueprints = self.app.config['INSTALLED_BLUEPRINTS']
        for blueprint_name in blueprints:
            bp = __import__('project.%s' % blueprint_name, fromlist=['views'])

            try:
                self.app.register_blueprint(bp.views.mod)
            except:
                pass


    def configure_extentions(self):
        db.init_app(self.app)
        login_manager.init_app(self.app)

    def run(self):
        self.app.run(host=self.app.config['HOST'],port=self.app.config['PORT'])