"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.resource_event import ResourceEvent

PostSeriesRequest: TypeAlias = ResourceEvent | Annotated[list[ResourceEvent], "Array of measurement objects with resource identifier and optional timestamp."]
"""PostSeriesRequest."""
