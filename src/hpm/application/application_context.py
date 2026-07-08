"""
Haryana Partition Manager (HPM)

Application context.

The ApplicationContext acts as the composition root for the
application. It owns long-lived services and exposes application
metadata to the presentation layer.
"""

from __future__ import annotations

from hpm.configuration.settings import Settings
from hpm.configuration.settings_service import SettingsService


class ApplicationContext:
    """
    Shared application context.

    This class owns application-wide services and provides
    a single access point for application configuration.
    """

    APPLICATION_NAME = "Haryana Partition Manager"
    APPLICATION_VERSION = "0.1.0"
    ORGANIZATION_NAME = "HPM Project"

    def __init__(self) -> None:
        """
        Initialize the application context.
        """

        self._settings_service = SettingsService()

    # ------------------------------------------------------------------
    # Services
    # ------------------------------------------------------------------

    @property
    def settings_service(
        self,
    ) -> SettingsService:
        """
        Return the settings service.
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
    # Application Information
    # ------------------------------------------------------------------

    @property
    def application_name(
        self,
    ) -> str:
        """
        Return the application name.
        """

        return self.APPLICATION_NAME

    @property
    def version(
        self,
    ) -> str:
        """
        Return the application version.
        """

        return self.APPLICATION_VERSION

    @property
    def organization(
        self,
    ) -> str:
        """
        Return the organization name.
        """

        return self.ORGANIZATION_NAME