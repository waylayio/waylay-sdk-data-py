"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.scalar_data import ScalarData


class LatestValue(WaylayBaseModel):
    """LatestValue."""

    timestamp: StrictInt = Field(
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds."
    )
    value: ScalarData | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
