"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictFloat,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class TimeseriesFilterValueBounds(WaylayBaseModel):
    """TimeseriesFilterValueBounds."""

    lower_bound: StrictFloat | StrictInt = Field(alias="lowerBound")
    upper_bound: StrictFloat | StrictInt = Field(alias="upperBound")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
