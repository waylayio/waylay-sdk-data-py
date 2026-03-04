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

from ..models.timestamped_event import TimestampedEvent


class MessageQueryResultItem(WaylayBaseModel):
    """MessageQueryResultItem."""

    resource: StrictStr | None = Field(
        default=None, description="Primary identifier of a _Resource_"
    )
    messages: list[TimestampedEvent] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
