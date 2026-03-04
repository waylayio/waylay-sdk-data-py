"""Waylay Broker model tests.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.data.models.message_query_result_item import (
        MessageQueryResultItem,
    )

    MessageQueryResultItemAdapter = TypeAdapter(MessageQueryResultItem)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

message_query_result_item_model_schema = json.loads(
    r"""{
  "title" : "MessageQueryResultItem",
  "type" : "object",
  "properties" : {
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "messages" : {
      "title" : "messages",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/TimestampedEvent"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
message_query_result_item_model_schema.update({"definitions": MODEL_DEFINITIONS})

message_query_result_item_faker = JSF(
    message_query_result_item_model_schema, allow_none_optionals=1
)


class MessageQueryResultItemStub:
    """MessageQueryResultItem unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return message_query_result_item_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "MessageQueryResultItem":
        """Create MessageQueryResultItem stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                MessageQueryResultItemAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return MessageQueryResultItemAdapter.validate_python(
            json, context={"skip_validation": True}
        )
