"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.publish_event_response_object_object import (
    PublishEventResponseObjectObject,
)
from ..models.timestamped_resource_event import TimestampedResourceEvent

PublishEventResponseContent: TypeAlias = TimestampedResourceEvent | Annotated[list[TimestampedResourceEvent], "Array of measurement objects with resource identifier and timestamp."] | PublishEventResponseObjectObject
"""PublishEventResponseContent."""
