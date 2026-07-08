"""
Haryana Partition Manager (HPM)

Partition Case domain entity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from datetime import datetime
from uuid import UUID
from uuid import uuid4


@dataclass(slots=True)
class PartitionCase:
    """
    Represents one partition proceeding.

    This is the aggregate root of the partition domain.
    """

    #
    # Identity
    #

    id: UUID = field(
        default_factory=uuid4,
    )

    #
    # Case Information
    #

    case_number: str = ""

    case_type: str = "General"

    order_number: str = ""

    order_date: date = field(
        default_factory=date.today,
    )

    revenue_officer: str = ""

    #
    # Revenue Information
    #

    village_code: str = ""

    village_name: str = ""

    jamabandi_year: str = ""

    #
    # Status
    #

    status: str = "Draft"

    remarks: str = ""

    #
    # Audit
    #

    created_at: datetime = field(
        default_factory=datetime.now,
    )

    modified_at: datetime = field(
        default_factory=datetime.now,
    )

    def touch(
        self,
    ) -> None:
        """
        Update the modification timestamp.
        """

        self.modified_at = datetime.now()