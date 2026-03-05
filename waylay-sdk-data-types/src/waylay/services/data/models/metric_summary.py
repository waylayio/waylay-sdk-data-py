"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.latest_value import LatestValue


class MetricSummary(WaylayBaseModel):
    """MetricSummary."""

    name: StrictStr = Field(
        description="Key that identifies a single timeseries for a given _Resource_. Corresponds with the top-level keys of _Message Events_  that are processed by the broker for that _Resource_."
    )
    latest: LatestValue | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
