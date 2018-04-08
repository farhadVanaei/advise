import os


class DefaultConfig(object):
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "SOMEKEY"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    VERSION = "1.0.0"
    MINIFY = False
    SECRET_KEY = 'somekey'
    INSTALLED_BLUEPRINTS = [
        'zone',
        'asset'
    ]
    PORT=8000
    HOST='0.0.0.0'


class DevelopmentConfig(DefaultConfig):
    SECRET_KEY = os.urandom(34)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:13306/advisor'
    DEBUG = True
