"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.publish_resource_event_response_object_object import (
    PublishResourceEventResponseObjectObject,
)
from ..models.timestamped_event import TimestampedEvent

PublishResourceEventResponseContent: TypeAlias = TimestampedEvent | PublishResourceEventResponseObjectObject
"""PublishResourceEventResponseContent."""
