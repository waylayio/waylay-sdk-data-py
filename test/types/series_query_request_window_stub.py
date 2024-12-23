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
    from waylay.services.data.models.series_query_request_window import (
        SeriesQueryRequestWindow,
    )

    SeriesQueryRequestWindowAdapter = TypeAdapter(SeriesQueryRequestWindow)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

series_query_request_window_model_schema = json.loads(
    r"""{
  "title" : "SeriesQueryRequest_window",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/DurationWithUnit"
  }, {
    "$ref" : "#/components/schemas/SO8601Duration"
  } ]
}
""",
    object_hook=with_example_provider,
)
series_query_request_window_model_schema.update({"definitions": MODEL_DEFINITIONS})

series_query_request_window_faker = JSF(
    series_query_request_window_model_schema, allow_none_optionals=1
)


class SeriesQueryRequestWindowStub:
    """SeriesQueryRequestWindow unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return series_query_request_window_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "SeriesQueryRequestWindow":
        """Create SeriesQueryRequestWindow stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SeriesQueryRequestWindowAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SeriesQueryRequestWindowAdapter.validate_python(
            json, context={"skip_validation": True}
        )
