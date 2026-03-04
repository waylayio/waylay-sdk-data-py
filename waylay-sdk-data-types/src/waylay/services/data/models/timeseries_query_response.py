"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.timeseries_json_result import TimeseriesJsonResult

TimeseriesQueryResponse: TypeAlias = TimeseriesJsonResult | list[TimeseriesJsonResult]
"""TimeseriesQueryResponse."""
