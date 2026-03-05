"""Waylay Broker model tests.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.data.models.raw_datapoints_response import (
        RawDatapointsResponse,
    )

    RawDatapointsResponseAdapter = TypeAdapter(RawDatapointsResponse)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

raw_datapoints_response_model_schema = json.loads(
    r"""{
  "required" : [ "query", "series" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/RawDatapointsLinks"
    },
    "query" : {
      "$ref" : "#/components/schemas/SeriesQueryResponse"
    },
    "series" : {
      "type" : "array",
      "description" : "Array of timestamp-value tuples",
      "items" : {
        "$ref" : "#/components/schemas/SeriesKeyValue"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
raw_datapoints_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

raw_datapoints_response_faker = JSF(
    raw_datapoints_response_model_schema, allow_none_optionals=1
)


class RawDatapointsResponseStub:
    """RawDatapointsResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return raw_datapoints_response_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "RawDatapointsResponse":
        """Create RawDatapointsResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                RawDatapointsResponseAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return RawDatapointsResponseAdapter.validate_python(
            json, context={"skip_validation": True}
        )
