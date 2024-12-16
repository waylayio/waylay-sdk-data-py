# coding: utf-8
"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.event_timestamp import EventTimestamp


class Event(WaylayBaseModel):
    """Measurement object with optional event timestamp.."""

    timestamp: EventTimestamp | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
