"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.timeseries_filter_value_bounds import TimeseriesFilterValueBounds
from ..models.timeseries_filter_value_exact import TimeseriesFilterValueExact

TimeseriesFilterValue: TypeAlias = TimeseriesFilterValueExact | TimeseriesFilterValueBounds
"""TimeseriesFilterValue."""
