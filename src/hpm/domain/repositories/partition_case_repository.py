"""
Haryana Partition Manager (HPM)

Partition Case repository interface.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from hpm.domain.entities.partition_case import PartitionCase


class PartitionCaseRepository(ABC):
    """
    Repository contract for partition cases.
    """

    @abstractmethod
    def add(
        self,
        partition_case: PartitionCase,
    ) -> None:
        """
        Store a new partition case.
        """
        raise NotImplementedError

    @abstractmethod
    def get(
        self,
        case_number: str,
    ) -> PartitionCase | None:
        """
        Return a partition case by case number.
        """
        raise NotImplementedError

    @abstractmethod
    def list_all(
        self,
    ) -> list[PartitionCase]:
        """
        Return all partition cases.
        """
        raise NotImplementedError

    @abstractmethod
    def update(
        self,
        partition_case: PartitionCase,
    ) -> None:
        """
        Update an existing partition case.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(
        self,
        case_number: str,
    ) -> None:
        """
        Delete a partition case.
        """
        raise NotImplementedError