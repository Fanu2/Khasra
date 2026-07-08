"""
Haryana Partition Manager (HPM)

SQLite database configuration.
"""

from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from hpm.configuration.settings import HPM_HOME


DATABASE_FILE = HPM_HOME / "database" / "hpm.db"


engine = create_engine(
    f"sqlite:///{DATABASE_FILE}",
    echo=False,
)


SessionFactory = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.
    """

    pass


def initialize_database() -> None:
    """
    Create all database tables.
    """

    Base.metadata.create_all(
        bind=engine,
    )