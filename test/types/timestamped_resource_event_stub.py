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
    from waylay.services.data.models.timestamped_resource_event import (
        TimestampedResourceEvent,
    )

    TimestampedResourceEventAdapter = TypeAdapter(TimestampedResourceEvent)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

timestamped_resource_event_model_schema = json.loads(
    r"""{
  "required" : [ "resource", "timestamp" ],
  "type" : "object",
  "properties" : {
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "timestamp" : {
      "description" : "Event timestamp",
      "allOf" : [ {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      } ]
    }
  },
  "additionalProperties" : {
    "$ref" : "#/components/schemas/Measurements"
  },
  "description" : "Measurement object with resource identifier and timestamp."
}
""",
    object_hook=with_example_provider,
)
timestamped_resource_event_model_schema.update({"definitions": MODEL_DEFINITIONS})

timestamped_resource_event_faker = JSF(
    timestamped_resource_event_model_schema, allow_none_optionals=1
)


class TimestampedResourceEventStub:
    """TimestampedResourceEvent unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return timestamped_resource_event_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "TimestampedResourceEvent":
        """Create TimestampedResourceEvent stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TimestampedResourceEventAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TimestampedResourceEventAdapter.validate_python(
            json, context={"skip_validation": True}
        )
