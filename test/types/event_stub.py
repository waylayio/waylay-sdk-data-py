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
    from waylay.services.data.models.event import Event

    EventAdapter = TypeAdapter(Event)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

event_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "timestamp" : {
      "$ref" : "#/components/schemas/Event_timestamp"
    }
  },
  "additionalProperties" : {
    "$ref" : "#/components/schemas/Measurements"
  },
  "description" : "Measurement object with optional event timestamp."
}
""",
    object_hook=with_example_provider,
)
event_model_schema.update({"definitions": MODEL_DEFINITIONS})

event_faker = JSF(event_model_schema, allow_none_optionals=1)


class EventStub:
    """Event unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return event_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Event":
        """Create Event stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(EventAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return EventAdapter.validate_python(json, context={"skip_validation": True})
