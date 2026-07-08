"""
Haryana Partition Manager (HPM)

Application context.

The ApplicationContext is the composition root of the application.
It owns long-lived services and exposes shared application resources
to the presentation layer.
"""

from __future__ import annotations

from hpm.configuration.settings import Settings
from hpm.configuration.settings_service import SettingsService


class ApplicationContext:
    """
    Shared application context.

    This class is responsible for creating and managing application-wide
    services. Presentation components should obtain shared services
    through this class instead of constructing them directly.
    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize the application context.
        """

        #
        # Core Services
        #

        self._settings_service = SettingsService()

        #
        # Future Services
        #
        # These will be registered as they are implemented.
        #
        # self._database = ...
        # self._partition_case_service = ...
        # self._logging_service = ...
        # self._report_service = ...
        #

    # ------------------------------------------------------------------
    # Core Services
    # ------------------------------------------------------------------

    @property
    def settings_service(
        self,
    ) -> SettingsService:
        """
        Return the application settings service.
        """

        return self._settings_service

    @property
    def settings(
        self,
    ) -> Settings:
        """
        Return the current application settings.
        """

        return self._settings_service.settings

    # ------------------------------------------------------------------
    # Application Metadata
    # ------------------------------------------------------------------

    @property
    def application_name(
        self,
    ) -> str:
        """
        Return the application name.
        """

        return self.settings.application_name

    @property
    def version(
        self,
    ) -> str:
        """
        Return the application version.
        """

        return self.settings.application_version

    @property
    def organization(
        self,
    ) -> str:
        """
        Return the organization name.
        """

        return self.settings.organization_name