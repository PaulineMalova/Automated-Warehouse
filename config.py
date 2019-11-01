import os


class Config(object):
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = False
    DEBUG = False
    SECRET_KEY = "e256afe2d4fa4be7b1705207c546f5ab"
    CSRF_ENABLED = True

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class StagingConfig(Config):
    """
    Staging configurations
    """

    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    "development": DevelopmentConfig,
    "staging": StagingConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
