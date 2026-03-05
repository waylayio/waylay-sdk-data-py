"""Waylay Broker models.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.message_query import MessageQuery
from ..models.message_query_result_item import MessageQueryResultItem


class MessageQueryResult(WaylayBaseModel):
    """MessageQueryResult."""

    query: MessageQuery | None = None
    results: list[MessageQueryResultItem] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
