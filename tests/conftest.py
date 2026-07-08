"""
Shared pytest fixtures for Haryana Partition Manager.
"""

from __future__ import annotations

import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from hpm.domain.entities.partition_case import PartitionCase
from hpm.infrastructure.persistence.sqlite.database import Base


@pytest.fixture
def partition_case() -> PartitionCase:
    """
    Return a sample partition case.
    """

    return PartitionCase(
        case_number="PT-2026-001",
        case_type="General",
        order_number="ORD-001",
        revenue_officer="Assistant Collector",
    )


@pytest.fixture
def session():
    """
    Return a temporary SQLite session for testing.
    """

    engine = create_engine(
        "sqlite:///:memory:",
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(
        bind=engine,
    )

    session = Session()

    try:
        yield session
    finally:
        session.close()