"""
Tests for the PartitionCase domain entity.
"""

from __future__ import annotations

from datetime import date
from datetime import datetime

from hpm.domain.entities.partition_case import PartitionCase


def test_default_partition_case() -> None:
    """
    Verify default values.
    """

    partition_case = PartitionCase()

    assert partition_case.case_number == ""
    assert partition_case.case_type == "General"
    assert partition_case.status == "Draft"
    assert partition_case.order_date == date.today()

    assert partition_case.id is not None

    assert isinstance(
        partition_case.created_at,
        datetime,
    )

    assert isinstance(
        partition_case.modified_at,
        datetime,
    )


def test_touch_updates_modified_time() -> None:
    """
    Verify touch() updates the modification timestamp.
    """

    partition_case = PartitionCase()

    original = partition_case.modified_at

    partition_case.touch()

    assert partition_case.modified_at >= original


def test_custom_case_number() -> None:
    """
    Verify custom values are stored.
    """

    partition_case = PartitionCase(
        case_number="PT-2026-001",
    )

    assert partition_case.case_number == "PT-2026-001"