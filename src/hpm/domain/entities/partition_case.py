"""
Haryana Partition Manager (HPM)

Partition Case entity.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class PartitionCase:
    """
    Represents a partition case.
    """

    case_number: str
    village_code: str
    village_name: str
    jamabandi_year: str

    status: str = "Draft"

    created_at: datetime | None = None
    modified_at: datetime | None = None

    remarks: str = ""

    def __post_init__(self) -> None:
        """
        Initialize timestamps.
        """

        now = datetime.now()

        if self.created_at is None:
            self.created_at = now

        if self.modified_at is None:
            self.modified_at = now