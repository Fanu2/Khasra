"""
Haryana Partition Manager (HPM)

Application dependency container.
"""

from __future__ import annotations


class ApplicationContext:
    """
    Root dependency container.

    This class owns application-wide dependencies.
    During early development it contains only the
    application metadata. Services and repositories
    will be registered here in later sprints.
    """

    def __init__(self) -> None:
        self._version = "0.1.0"
        self._application_name = "Haryana Partition Manager"

    @property
    def application_name(self) -> str:
        """
        Return the application name.
        """
        return self._application_name

    @property
    def version(self) -> str:
        """
        Return the application version.
        """
        return self._version