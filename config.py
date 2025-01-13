import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')  # Replace with a secure key for production
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///app.db')  # Default to SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SUPPORT_EMAIL = 'support@yourdomain.com'  # Replace with your support email
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # Directory for uploaded files
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB upload limit
    AI_SERVICE_API_KEY = os.environ.get('AI_SERVICE_API_KEY', '')  # API key for AI services, if any


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Log SQL statements for debugging


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use in-memory database for tests
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing forms


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///app.db')  # Use environment variable for DB


# Optionally, you can define a mapping for easy configuration switching.
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
