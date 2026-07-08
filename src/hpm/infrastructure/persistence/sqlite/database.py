"""
Haryana Partition Manager (HPM)

SQLite database configuration.
"""

from __future__ import annotations

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


DATABASE_DIR = Path.home() / ".hpm"
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_FILE = DATABASE_DIR / "hpm.db"


engine = create_engine(
    f"sqlite:///{DATABASE_FILE}",
    echo=False,
    future=True,
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    """
    Base class for SQLAlchemy models.
    """

    pass


def create_database() -> None:
    """
    Create all database tables.
    """

    Base.metadata.create_all(bind=engine)