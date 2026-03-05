"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.series_query_request import SeriesQueryRequest
from ..models.series_query_without_aggregates_request import (
    SeriesQueryWithoutAggregatesRequest,
)

SeriesQueryItem: TypeAlias = SeriesQueryRequest | SeriesQueryWithoutAggregatesRequest
"""SeriesQueryItem."""
