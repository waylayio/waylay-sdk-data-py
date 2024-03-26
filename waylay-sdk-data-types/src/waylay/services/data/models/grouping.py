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

from ..models.grouping_any_of import GroupingAnyOf

Grouping = Union[
    Annotated[GroupingAnyOf, ""],
    Annotated[str, "Time interval with duration unit."],
    Annotated[
        str,
        "A [ISO8601 Duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) with day (`D`), hour (`H`), minute (`M`) and second (`S`) specifiers.",
    ],
]
"""Grouping."""
