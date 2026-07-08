"""
Haryana Partition Manager (HPM)

Application context.
"""

from __future__ import annotations

from hpm.configuration.settings import Settings
from hpm.configuration.settings_service import SettingsService


class ApplicationContext:
    """
    Shared application services.
    """

    def __init__(self) -> None:

        self._settings_service = SettingsService()

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
        Return the current settings.
        """

        return self._settings_service.settings

    @property
    def application_name(
        self,
    ) -> str:
        """
        Return the application name.
        """

        return self.settings.application_name