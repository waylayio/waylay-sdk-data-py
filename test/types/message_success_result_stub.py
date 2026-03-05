"""Waylay Broker model tests.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.data.models.message_success_result import MessageSuccessResult

    MessageSuccessResultAdapter = TypeAdapter(MessageSuccessResult)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

message_success_result_model_schema = json.loads(
    r"""{
  "required" : [ "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
message_success_result_model_schema.update({"definitions": MODEL_DEFINITIONS})

message_success_result_faker = JSF(
    message_success_result_model_schema, allow_none_optionals=1
)


class MessageSuccessResultStub:
    """MessageSuccessResult unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return message_success_result_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "MessageSuccessResult":
        """Create MessageSuccessResult stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                MessageSuccessResultAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return MessageSuccessResultAdapter.validate_python(
            json, context={"skip_validation": True}
        )
