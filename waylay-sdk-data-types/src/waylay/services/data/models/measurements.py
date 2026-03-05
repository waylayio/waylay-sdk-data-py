"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias, Union

from ..models.scalar_data import ScalarData

Measurements: TypeAlias = Union[ScalarData, "ObjectData"]
"""Values in an _Event_ payload. Note that only _scalar_ data is stored in the timeseries, while Arrays and objects are only stored in the _Message Cache_.."""

from ..models.object_data import ObjectData  # noqa  # postponed import due to cyclic reference
