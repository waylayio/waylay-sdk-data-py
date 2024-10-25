# coding: utf-8
"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.timestamped_event import TimestampedEvent


class MessageQueryResultResultsInner(WaylayBaseModel):
    """MessageQueryResultResultsInner."""

    resource: StrictStr | None = Field(
        default=None, description="Primary identifier of a _Resource_"
    )
    messages: List[TimestampedEvent] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
