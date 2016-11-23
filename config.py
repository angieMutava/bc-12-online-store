import os
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """
    Default configuration
    """
    DEBUG = False
    # Secret Key from random number generator
    SECRET_KEY = '\xfa\xc7\t\x0f\x05O\xf7\xf0\x8d\xf3%\xc4i\xca\xf6Q\xc2\x15c\t\xfc\x13N\xc9'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app/static/img/uploads/')
    # ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


class DevelopmentConfig(BaseConfig):
    """
    Configuration for development environment
    """
    DEBUG = True  # Ensure debug mode is active during development


class ProductionConfig(BaseConfig):
    """
    Configuration for production environment
    """
    DEBUG = False  # Ensure debug mode is deactivated during production
