"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.order import Order
from ..models.series_query_request_from import SeriesQueryRequestFrom
from ..models.series_query_request_window import SeriesQueryRequestWindow
from ..models.timeseries_filter import TimeseriesFilter


class SeriesQueryWithoutAggregatesRequest(WaylayBaseModel):
    """SeriesQueryWithoutAggregatesRequest."""

    var_from: SeriesQueryRequestFrom | None = Field(default=None, alias="from")
    until: SeriesQueryRequestFrom | None = None
    window: SeriesQueryRequestWindow | None = None
    metric: StrictStr = Field(
        description="Key that identifies a single timeseries for a given _Resource_. Corresponds with the top-level keys of _Message Events_  that are processed by the broker for that _Resource_."
    )
    aggregates: Annotated[list[Any], Field(min_length=0, max_length=0)] | None = None
    resources: Annotated[list[StrictStr], Field(min_length=1, max_length=1)]
    max_results: Annotated[int, Field(strict=True, ge=0)] | None = Field(
        default=None, alias="maxResults"
    )
    filter: TimeseriesFilter | None = None
    order: Order | None = Order.ASCENDING
    return_ingestion_timestamp: StrictBool | None = Field(
        default=False, alias="returnIngestionTimestamp"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
