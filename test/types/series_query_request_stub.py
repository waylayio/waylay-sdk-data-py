# coding: utf-8
"""Waylay Broker model tests.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.data.models.series_query_request import SeriesQueryRequest

    SeriesQueryRequestAdapter = TypeAdapter(SeriesQueryRequest)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

series_query_request_model_schema = json.loads(
    r"""{
  "required" : [ "aggregates", "metric", "resources" ],
  "type" : "object",
  "properties" : {
    "from" : {
      "$ref" : "#/components/schemas/SeriesQueryRequest_from"
    },
    "until" : {
      "$ref" : "#/components/schemas/SeriesQueryRequest_from"
    },
    "window" : {
      "$ref" : "#/components/schemas/SeriesQueryRequest_window"
    },
    "metric" : {
      "$ref" : "#/components/schemas/MetricId"
    },
    "aggregates" : {
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Aggregate"
      }
    },
    "grouping" : {
      "$ref" : "#/components/schemas/Grouping"
    },
    "resources" : {
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/ResourceId"
      }
    },
    "maxResults" : {
      "minimum" : 0,
      "type" : "integer"
    },
    "filter" : {
      "$ref" : "#/components/schemas/TimeseriesFilter"
    },
    "order" : {
      "$ref" : "#/components/schemas/Order"
    }
  }
}
""",
    object_hook=with_example_provider,
)
series_query_request_model_schema.update({"definitions": MODEL_DEFINITIONS})

series_query_request_faker = JSF(
    series_query_request_model_schema, allow_none_optionals=1
)


class SeriesQueryRequestStub:
    """SeriesQueryRequest unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return series_query_request_faker.generate()

    @classmethod
    def create_instance(cls) -> "SeriesQueryRequest":
        """Create SeriesQueryRequest stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return SeriesQueryRequestAdapter.validate_python(cls.create_json())
