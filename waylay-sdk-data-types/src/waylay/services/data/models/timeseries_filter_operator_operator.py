"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class TimeseriesFilterOperatorOperator(str, Enum):
    """TimeseriesFilterOperatorOperator."""

    GT = "gt"
    GTE = "gte"
    LT = "lt"
    LTE = "lte"
    EQ = "eq"
    NE = "ne"
    BETWEEN = "between"

    def __str__(self) -> str:
        return str(self.value)
