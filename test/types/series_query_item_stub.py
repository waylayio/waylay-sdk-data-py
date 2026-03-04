"""Waylay Broker model tests.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.data.models.series_query_item import SeriesQueryItem

    SeriesQueryItemAdapter = TypeAdapter(SeriesQueryItem)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

series_query_item_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/SeriesQueryRequest"
  }, {
    "$ref" : "#/components/schemas/SeriesQueryWithoutAggregatesRequest"
  } ]
}
""",
    object_hook=with_example_provider,
)
series_query_item_model_schema.update({"definitions": MODEL_DEFINITIONS})

series_query_item_faker = JSF(series_query_item_model_schema, allow_none_optionals=1)


class SeriesQueryItemStub:
    """SeriesQueryItem unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return series_query_item_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "SeriesQueryItem":
        """Create SeriesQueryItem stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SeriesQueryItemAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SeriesQueryItemAdapter.validate_python(
            json, context={"skip_validation": True}
        )
