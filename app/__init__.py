from flask import Flask
from sqlalchemy import create_engine, event
from sqlalchemy.orm import scoped_session, sessionmaker

# Initialize SQLAlchemy
engine = create_engine("postgresql://postgres:postgres@localhost:5432/flaskloginapp")
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    
    # Add configuration if needed
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/flaskloginapp"
    
    # Attach the session to the app's request lifecycle
    @app.teardown_appcontext
    def remove_session(exception=None):
        """Remove the database session at the end of the request."""
        SessionLocal.remove()

    return app