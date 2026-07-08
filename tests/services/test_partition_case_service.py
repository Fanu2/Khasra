"""
Tests for the PartitionCaseService.
"""

from __future__ import annotations

import pytest

from hpm.application.services.partition_case_service import (
    PartitionCaseService,
)


def test_create_case(
    session,
    partition_case,
) -> None:
    """
    Verify a new case can be created.
    """

    from hpm.infrastructure.persistence.sqlite.repositories.sqlite_partition_case_repository import (
        SqlitePartitionCaseRepository,
    )

    repository = SqlitePartitionCaseRepository(session)

    service = PartitionCaseService(repository)

    service.create_case(partition_case)

    loaded = service.open_case(
        partition_case.case_number,
    )

    assert loaded is not None
    assert loaded.case_number == partition_case.case_number


def test_duplicate_case_number(
    session,
    partition_case,
) -> None:
    """
    Duplicate case numbers are rejected.
    """

    from hpm.infrastructure.persistence.sqlite.repositories.sqlite_partition_case_repository import (
        SqlitePartitionCaseRepository,
    )

    repository = SqlitePartitionCaseRepository(session)

    service = PartitionCaseService(repository)

    service.create_case(partition_case)

    with pytest.raises(ValueError):
        service.create_case(partition_case)