"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.series_query_response import SeriesQueryResponse
from ..models.series_value import SeriesValue


class TimeseriesJsonResult(WaylayBaseModel):
    """TimeseriesJsonResult."""

    query: SeriesQueryResponse
    series: list[
        Annotated[list[SeriesValue | None], Field(min_length=2, max_length=2)]
    ] = Field(description="Array of timestamp-value tuples")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
