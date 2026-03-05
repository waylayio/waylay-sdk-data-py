"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, TypeAlias

GetMetricSeriesFromParameter: TypeAlias = Annotated[int, "Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds."] | datetime
"""GetMetricSeriesFromParameter."""
