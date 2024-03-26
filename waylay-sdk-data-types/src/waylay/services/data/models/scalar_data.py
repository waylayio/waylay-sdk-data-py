# coding: utf-8
"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import (
    Union,
)

from typing_extensions import (
    Annotated,  # >=3.9
)

ScalarData = Union[Annotated[float, ""], Annotated[str, ""], Annotated[bool, ""]]
"""Event data stored in both the _Message Cache_ and _Time Series Database_. Keys of these measurements become a _Metric_ for the resource.."""
