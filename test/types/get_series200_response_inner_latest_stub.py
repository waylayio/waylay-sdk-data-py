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
    from waylay.services.data.models.get_series200_response_inner_latest import (
        GetSeries200ResponseInnerLatest,
    )

    GetSeries200ResponseInnerLatestAdapter = TypeAdapter(
        GetSeries200ResponseInnerLatest
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

get_series_200_response_inner_latest_model_schema = json.loads(
    r"""{
  "required" : [ "timestamp" ],
  "type" : "object",
  "properties" : {
    "timestamp" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    },
    "value" : {
      "$ref" : "#/components/schemas/ScalarData"
    }
  }
}
""",
    object_hook=with_example_provider,
)
get_series_200_response_inner_latest_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

get_series_200_response_inner_latest_faker = JSF(
    get_series_200_response_inner_latest_model_schema, allow_none_optionals=1
)


class GetSeries200ResponseInnerLatestStub:
    """GetSeries200ResponseInnerLatest unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_series_200_response_inner_latest_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "GetSeries200ResponseInnerLatest":
        """Create GetSeries200ResponseInnerLatest stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GetSeries200ResponseInnerLatestAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GetSeries200ResponseInnerLatestAdapter.validate_python(
            json, context={"skip_validation": True}
        )
