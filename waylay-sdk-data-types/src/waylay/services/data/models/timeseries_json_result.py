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
)
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.series_key_value_inner import SeriesKeyValueInner
from ..models.series_query_response import SeriesQueryResponse


class TimeseriesJsonResult(WaylayBaseModel):
    """TimeseriesJsonResult."""

    query: SeriesQueryResponse
    series: List[
        Annotated[List[SeriesKeyValueInner], Field(min_length=2, max_length=2)]
    ] = Field(description="Array of timestamp-value tuples")

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
