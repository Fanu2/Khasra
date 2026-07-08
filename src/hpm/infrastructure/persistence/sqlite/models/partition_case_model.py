"""
Haryana Partition Manager (HPM)

Partition Case SQLAlchemy model.
"""

from __future__ import annotations

from datetime import date
from datetime import datetime

from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from hpm.infrastructure.persistence.sqlite.database import Base


class PartitionCaseModel(Base):
    """
    SQLAlchemy model for partition cases.
    """

    __tablename__ = "partition_cases"

    #
    # Identity
    #

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    #
    # Case Information
    #

    case_number: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
    )

    case_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    order_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    order_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    revenue_officer: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    #
    # Revenue Information
    #

    village_code: Mapped[str] = mapped_column(
        String(20),
        default="",
    )

    village_name: Mapped[str] = mapped_column(
        String(150),
        default="",
    )

    jamabandi_year: Mapped[str] = mapped_column(
        String(20),
        default="",
    )

    #
    # Status
    #

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="Draft",
    )

    remarks: Mapped[str] = mapped_column(
        String(1000),
        default="",
    )

    #
    # Audit
    #

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    modified_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )