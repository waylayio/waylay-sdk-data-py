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
    from waylay.services.data.models.message_query_result import MessageQueryResult

    MessageQueryResultAdapter = TypeAdapter(MessageQueryResult)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

message_query_result_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "query" : {
      "$ref" : "#/components/schemas/MessageQuery"
    },
    "results" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/MessageQueryResult_results_inner"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
message_query_result_model_schema.update({"definitions": MODEL_DEFINITIONS})

message_query_result_faker = JSF(
    message_query_result_model_schema, allow_none_optionals=1
)


class MessageQueryResultStub:
    """MessageQueryResult unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return message_query_result_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "MessageQueryResult":
        """Create MessageQueryResult stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                MessageQueryResultAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return MessageQueryResultAdapter.validate_python(
            json, context={"skip_validation": True}
        )
