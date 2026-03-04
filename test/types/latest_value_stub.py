"""Waylay Broker model tests.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.data.models.latest_value import LatestValue

    LatestValueAdapter = TypeAdapter(LatestValue)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

latest_value_model_schema = json.loads(
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
latest_value_model_schema.update({"definitions": MODEL_DEFINITIONS})

latest_value_faker = JSF(latest_value_model_schema, allow_none_optionals=1)


class LatestValueStub:
    """LatestValue unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return latest_value_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "LatestValue":
        """Create LatestValue stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(LatestValueAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return LatestValueAdapter.validate_python(
            json, context={"skip_validation": True}
        )
