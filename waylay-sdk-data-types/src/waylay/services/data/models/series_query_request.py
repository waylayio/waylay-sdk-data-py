# coding: utf-8
"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.aggregate import Aggregate
from ..models.grouping import Grouping
from ..models.order import Order
from ..models.series_query_request_from import SeriesQueryRequestFrom
from ..models.series_query_request_window import SeriesQueryRequestWindow
from ..models.timeseries_filter import TimeseriesFilter


class SeriesQueryRequest(WaylayBaseModel):
    """SeriesQueryRequest."""

    var_from: SeriesQueryRequestFrom | None = Field(default=None, alias="from")
    until: SeriesQueryRequestFrom | None = None
    window: SeriesQueryRequestWindow | None = None
    metric: StrictStr = Field(
        description="Key that identifies a single timeseries for a given _Resource_. Corresponds with the top-level keys of _Message Events_  that are processed by the broker for that _Resource_."
    )
    aggregates: Annotated[List[Aggregate], Field(min_length=1)]
    grouping: Grouping | None = None
    resources: Annotated[List[StrictStr], Field(min_length=1)]
    max_results: Annotated[int, Field(strict=True, ge=0)] | None = Field(
        default=None, alias="maxResults"
    )
    filter: TimeseriesFilter | None = None
    order: Order | None = None

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
