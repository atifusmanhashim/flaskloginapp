import os

class Config:
    """Configuration for the Flask application."""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/flaskloginapp")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
