"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class GroupingAuto(str, Enum):
    """GroupingAuto."""

    AUTO = "auto"

    def __str__(self) -> str:
        return str(self.value)
