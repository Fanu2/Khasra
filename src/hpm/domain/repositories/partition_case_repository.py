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
    Repository interface for partition cases.
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
    def get_by_id(
        self,
        case_id: str,
    ) -> PartitionCase | None:
        """
        Return a partition case by its unique identifier.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_case_number(
        self,
        case_number: str,
    ) -> PartitionCase | None:
        """
        Return a partition case by its case number.
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
        case_id: str,
    ) -> None:
        """
        Delete a partition case.
        """
        raise NotImplementedError

    @abstractmethod
    def exists(
        self,
        case_number: str,
    ) -> bool:
        """
        Return True if the case number already exists.
        """
        raise NotImplementedError