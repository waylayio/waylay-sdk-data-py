"""Waylay Broker model tests.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.data.models.raw_datapoints_links import RawDatapointsLinks

    RawDatapointsLinksAdapter = TypeAdapter(RawDatapointsLinks)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

raw_datapoints_links_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "next" : {
      "$ref" : "#/components/schemas/HalLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
raw_datapoints_links_model_schema.update({"definitions": MODEL_DEFINITIONS})

raw_datapoints_links_faker = JSF(
    raw_datapoints_links_model_schema, allow_none_optionals=1
)


class RawDatapointsLinksStub:
    """RawDatapointsLinks unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return raw_datapoints_links_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "RawDatapointsLinks":
        """Create RawDatapointsLinks stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                RawDatapointsLinksAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return RawDatapointsLinksAdapter.validate_python(
            json, context={"skip_validation": True}
        )
