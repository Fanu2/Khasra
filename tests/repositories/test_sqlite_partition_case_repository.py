"""
Tests for the SQLite Partition Case repository.
"""

from __future__ import annotations

from hpm.infrastructure.persistence.sqlite.repositories.sqlite_partition_case_repository import (
    SqlitePartitionCaseRepository,
)


def test_add_partition_case(
    session,
    partition_case,
) -> None:
    """
    Verify a partition case can be saved and retrieved.
    """

    repository = SqlitePartitionCaseRepository(
        session,
    )

    repository.add(
        partition_case,
    )

    loaded = repository.get_by_case_number(
        partition_case.case_number,
    )

    assert loaded is not None

    assert (
        loaded.case_number
        == partition_case.case_number
    )

    assert (
        loaded.order_number
        == partition_case.order_number
    )

    assert (
        loaded.revenue_officer
        == partition_case.revenue_officer
    )