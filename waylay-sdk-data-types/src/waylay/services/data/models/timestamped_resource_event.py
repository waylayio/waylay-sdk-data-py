# coding: utf-8
"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class TimestampedResourceEvent(WaylayBaseModel):
    """Measurement object with resource identifier and timestamp.."""

    resource: StrictStr = Field(description="Primary identifier of a _Resource_")
    timestamp: StrictInt = Field(
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
