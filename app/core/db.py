from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import get_settings

settings = get_settings()

# Create SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[Session, None, None]:
    """
    Dependency function that yields database sessions.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()