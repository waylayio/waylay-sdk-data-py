"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias, Union

ObjectData: TypeAlias = Union[object, "list[Measurements]"]
"""Event data stored only in the _Message Cache_.."""

from ..models.measurements import Measurements  # noqa  # postponed import due to cyclic reference
