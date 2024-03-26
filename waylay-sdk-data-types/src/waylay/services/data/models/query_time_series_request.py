# coding: utf-8
"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import (
    List,
    Union,
)

from typing_extensions import (
    Annotated,  # >=3.9
)

from ..models.series_query_request import SeriesQueryRequest

QueryTimeSeriesRequest = Union[
    Annotated[SeriesQueryRequest, ""], Annotated[List[SeriesQueryRequest], ""]
]
"""QueryTimeSeriesRequest."""
