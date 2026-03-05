"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, TypeAlias

MessageQueryWindow: TypeAlias = Annotated[str, "Time interval with duration unit."] | datetime
"""A duration expression. Will be evaluated vs `from`, `until` or the query execution date to get the actual time range."""
