"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.timeseries_filter_value_exact_value import TimeseriesFilterValueExactValue


class TimeseriesFilterValueExact(WaylayBaseModel):
    """TimeseriesFilterValueExact."""

    value: TimeseriesFilterValueExactValue

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
