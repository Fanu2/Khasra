"""
Haryana Partition Manager (HPM)

Partition Case mapper.
"""

from __future__ import annotations

from uuid import UUID

from hpm.domain.entities.partition_case import PartitionCase
from hpm.infrastructure.persistence.sqlite.models.partition_case_model import (
    PartitionCaseModel,
)


class PartitionCaseMapper:
    """
    Maps between domain entities and SQLAlchemy models.
    """

    @staticmethod
    def to_model(
        entity: PartitionCase,
    ) -> PartitionCaseModel:
        """
        Convert a domain entity to a SQLAlchemy model.
        """

        return PartitionCaseModel(
            id=str(entity.id),
            case_number=entity.case_number,
            case_type=entity.case_type,
            order_number=entity.order_number,
            order_date=entity.order_date,
            revenue_officer=entity.revenue_officer,
            village_code=entity.village_code,
            village_name=entity.village_name,
            jamabandi_year=entity.jamabandi_year,
            status=entity.status,
            remarks=entity.remarks,
            created_at=entity.created_at,
            modified_at=entity.modified_at,
        )

    @staticmethod
    def to_entity(
        model: PartitionCaseModel,
    ) -> PartitionCase:
        """
        Convert a SQLAlchemy model to a domain entity.
        """

        return PartitionCase(
            id=UUID(model.id),
            case_number=model.case_number,
            case_type=model.case_type,
            order_number=model.order_number,
            order_date=model.order_date,
            revenue_officer=model.revenue_officer,
            village_code=model.village_code,
            village_name=model.village_name,
            jamabandi_year=model.jamabandi_year,
            status=model.status,
            remarks=model.remarks,
            created_at=model.created_at,
            modified_at=model.modified_at,
        )