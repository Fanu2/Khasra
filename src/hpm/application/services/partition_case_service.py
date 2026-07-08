"""
Haryana Partition Manager (HPM)

Partition Case application service.
"""

from __future__ import annotations

from hpm.domain.entities.partition_case import PartitionCase
from hpm.domain.repositories.partition_case_repository import (
    PartitionCaseRepository,
)


class PartitionCaseService:
    """
    Application service for partition cases.
    """

    def __init__(
        self,
        repository: PartitionCaseRepository,
    ) -> None:
        """
        Initialize the service.
        """

        self._repository = repository

    def create_case(
        self,
        partition_case: PartitionCase,
    ) -> None:
        """
        Create a new partition case.
        """

        if self._repository.exists(
            partition_case.case_number,
        ):
            raise ValueError(
                f"Case number '{partition_case.case_number}' already exists."
            )

        self._repository.add(
            partition_case,
        )

    def open_case(
        self,
        case_number: str,
    ) -> PartitionCase | None:
        """
        Open a partition case.
        """

        return self._repository.get_by_case_number(
            case_number,
        )

    def list_cases(
        self,
    ) -> list[PartitionCase]:
        """
        Return all partition cases.
        """

        return self._repository.list_all()

    def save_case(
        self,
        partition_case: PartitionCase,
    ) -> None:
        """
        Save changes to a partition case.
        """

        partition_case.touch()

        self._repository.update(
            partition_case,
        )

    def delete_case(
        self,
        partition_case: PartitionCase,
    ) -> None:
        """
        Delete a partition case.
        """

        self._repository.delete(
            partition_case.id,
        )