"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.event import Event

PostSeriesForResourceRequest: TypeAlias = Event | Annotated[list[Event], "Array of measurement objects with optional event timestamp."]
"""PostSeriesForResourceRequest."""
