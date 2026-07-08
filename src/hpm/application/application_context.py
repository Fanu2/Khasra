"""
Haryana Partition Manager (HPM)

Application context.

The ApplicationContext is the composition root of the application.
It owns long-lived services and exposes shared resources to the
presentation layer.
"""

from __future__ import annotations

from hpm.application.services.partition_case_service import (
    PartitionCaseService,
)
from hpm.configuration.settings import Settings
from hpm.configuration.settings_service import SettingsService
from hpm.infrastructure.persistence.sqlite.database import (
    SessionFactory,
    initialize_database,
)
from hpm.infrastructure.persistence.sqlite.repositories.sqlite_partition_case_repository import (
    SqlitePartitionCaseRepository,
)


class ApplicationContext:
    """
    Shared application context.

    Responsible for constructing and exposing all application-wide
    services.
    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize the application context.
        """

        #
        # Configuration
        #

        self._settings_service = SettingsService()

        #
        # Database
        #

        initialize_database()

        self._session = SessionFactory()

        #
        # Repositories
        #

        self._partition_case_repository = (
            SqlitePartitionCaseRepository(
                self._session,
            )
        )

        #
        # Application Services
        #

        self._partition_case_service = (
            PartitionCaseService(
                self._partition_case_repository,
            )
        )

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    @property
    def settings_service(
        self,
    ) -> SettingsService:

        return self._settings_service

    @property
    def settings(
        self,
    ) -> Settings:

        return self._settings_service.settings

    # ------------------------------------------------------------------
    # Services
    # ------------------------------------------------------------------

    @property
    def partition_case_service(
        self,
    ) -> PartitionCaseService:
        """
        Return the Partition Case application service.
        """

        return self._partition_case_service

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    @property
    def application_name(
        self,
    ) -> str:

        return self.settings.application_name

    @property
    def version(
        self,
    ) -> str:

        return self.settings.application_version

    @property
    def organization(
        self,
    ) -> str:

        return self.settings.organization_name