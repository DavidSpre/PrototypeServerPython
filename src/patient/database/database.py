from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

# naturally shouldn't be done in a real app, just for demonstration purposes
DATABASE_PASSWORD = "p"

DATABASE_URL = (
    f"postgresql+psycopg://postgres:{DATABASE_PASSWORD}@localhost:5432/postgres"
)

# database configuration
engine = create_engine(
    DATABASE_URL,
    # log all statements
    echo=True,
    # test connection for liveness upon checkout
    pool_pre_ping=True,
)

# database sessions
SessionLocal = sessionmaker(
    bind=engine,
)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
