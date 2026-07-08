"""
Haryana Partition Manager (HPM)

SQLite implementation of the Partition Case repository.
"""

from __future__ import annotations

from uuid import UUID

from sqlalchemy.orm import Session

from hpm.domain.entities.partition_case import PartitionCase
from hpm.domain.repositories.partition_case_repository import (
    PartitionCaseRepository,
)
from hpm.infrastructure.persistence.sqlite.mappers.partition_case_mapper import (
    PartitionCaseMapper,
)
from hpm.infrastructure.persistence.sqlite.models.partition_case_model import (
    PartitionCaseModel,
)


class SqlitePartitionCaseRepository(
    PartitionCaseRepository,
):
    """
    SQLite repository for partition cases.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:

        self._session = session

    def add(
        self,
        partition_case: PartitionCase,
    ) -> None:

        model = PartitionCaseMapper.to_model(
            partition_case,
        )

        self._session.add(
            model,
        )

        self._session.commit()

    def get_by_id(
        self,
        case_id: UUID,
    ) -> PartitionCase | None:

        model = self._session.get(
            PartitionCaseModel,
            str(case_id),
        )

        if model is None:
            return None

        return PartitionCaseMapper.to_entity(
            model,
        )

    def get_by_case_number(
        self,
        case_number: str,
    ) -> PartitionCase | None:

        model = (
            self._session.query(
                PartitionCaseModel,
            )
            .filter_by(
                case_number=case_number,
            )
            .first()
        )

        if model is None:
            return None

        return PartitionCaseMapper.to_entity(
            model,
        )

    def list_all(
        self,
    ) -> list[PartitionCase]:

        models = (
            self._session.query(
                PartitionCaseModel,
            )
            .order_by(
                PartitionCaseModel.case_number,
            )
            .all()
        )

        return [
            PartitionCaseMapper.to_entity(
                model,
            )
            for model in models
        ]

    def update(
        self,
        partition_case: PartitionCase,
    ) -> None:

        model = self._session.get(
            PartitionCaseModel,
            str(partition_case.id),
        )

        if model is None:
            raise ValueError(
                "Partition case not found.",
            )

        updated = PartitionCaseMapper.to_model(
            partition_case,
        )

        for attribute in (
            "case_number",
            "case_type",
            "order_number",
            "order_date",
            "revenue_officer",
            "village_code",
            "village_name",
            "jamabandi_year",
            "status",
            "remarks",
            "created_at",
            "modified_at",
        ):
            setattr(
                model,
                attribute,
                getattr(updated, attribute),
            )

        self._session.commit()

    def delete(
        self,
        case_id: UUID,
    ) -> None:

        model = self._session.get(
            PartitionCaseModel,
            str(case_id),
        )

        if model is None:
            return

        self._session.delete(
            model,
        )

        self._session.commit()

    def exists(
        self,
        case_number: str,
    ) -> bool:

        return (
            self._session.query(
                PartitionCaseModel,
            )
            .filter_by(
                case_number=case_number,
            )
            .first()
            is not None
        )