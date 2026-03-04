"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.publish_event_response_content import PublishEventResponseContent


class PublishEventResponse(WaylayBaseModel):
    """PublishEventResponse."""

    message: StrictStr | None = None
    content: PublishEventResponseContent | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
