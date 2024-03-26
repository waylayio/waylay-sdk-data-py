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
    from waylay.services.data.models.get_series200_response_inner import (
        GetSeries200ResponseInner,
    )

    GetSeries200ResponseInnerAdapter = TypeAdapter(GetSeries200ResponseInner)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

get_series_200_response_inner_model_schema = json.loads(
    r"""{
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/MetricId"
    },
    "latest" : {
      "$ref" : "#/components/schemas/getSeries_200_response_inner_latest"
    }
  }
}
""",
    object_hook=with_example_provider,
)
get_series_200_response_inner_model_schema.update({"definitions": MODEL_DEFINITIONS})

get_series_200_response_inner_faker = JSF(
    get_series_200_response_inner_model_schema, allow_none_optionals=1
)


class GetSeries200ResponseInnerStub:
    """GetSeries200ResponseInner unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_series_200_response_inner_faker.generate()

    @classmethod
    def create_instance(cls) -> "GetSeries200ResponseInner":
        """Create GetSeries200ResponseInner stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return GetSeries200ResponseInnerAdapter.validate_python(cls.create_json())
