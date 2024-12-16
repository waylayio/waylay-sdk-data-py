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
    from waylay.services.data.models.event_timestamp import EventTimestamp

    EventTimestampAdapter = TypeAdapter(EventTimestamp)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

event_timestamp_model_schema = json.loads(
    r"""{
  "title" : "Event_timestamp",
  "description" : "Event timestamp, if not specified, the _processing timestamp_\nof the broker will added as `timestamp` attribute.",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/SO8601Timestamp"
  } ]
}
""",
    object_hook=with_example_provider,
)
event_timestamp_model_schema.update({"definitions": MODEL_DEFINITIONS})

event_timestamp_faker = JSF(event_timestamp_model_schema, allow_none_optionals=1)


class EventTimestampStub:
    """EventTimestamp unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return event_timestamp_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "EventTimestamp":
        """Create EventTimestamp stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                EventTimestampAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return EventTimestampAdapter.validate_python(
            json, context={"skip_validation": True}
        )
