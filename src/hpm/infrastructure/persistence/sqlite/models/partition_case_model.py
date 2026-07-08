"""
Haryana Partition Manager (HPM)

SQLAlchemy model for partition cases.
"""

from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from hpm.infrastructure.persistence.sqlite.database import Base


class PartitionCaseModel(Base):
    """
    Database representation of a partition case.
    """

    __tablename__ = "partition_cases"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    case_number: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
    )

    village_code: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    village_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    jamabandi_year: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="Draft",
    )

    remarks: Mapped[str] = mapped_column(
        String(500),
        default="",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
    )

    modified_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
    )