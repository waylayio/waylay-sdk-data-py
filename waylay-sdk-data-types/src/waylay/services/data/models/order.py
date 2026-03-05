"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class Order(str, Enum):
    """the order in which the data is returned."""

    ASCENDING = "ascending"
    DESCENDING = "descending"

    def __str__(self) -> str:
        return str(self.value)
