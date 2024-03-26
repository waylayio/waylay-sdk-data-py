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
    StrictStr,
)
from waylay.sdk.api._models import _BaseModel

from ..models.event_timestamp import EventTimestamp


class ResourceEvent(_BaseModel):
    """Measurement object with resource identifier and optional timestamp.."""

    resource: StrictStr = Field(description="Primary identifier of a _Resource_")
    timestamp: EventTimestamp | None = None

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
    )
