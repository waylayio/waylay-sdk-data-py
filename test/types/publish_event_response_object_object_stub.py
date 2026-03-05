"""Waylay Broker model tests.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.data.models.publish_event_response_object_object import (
        PublishEventResponseObjectObject,
    )

    PublishEventResponseObjectObjectAdapter = TypeAdapter(
        PublishEventResponseObjectObject
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

publish_event_response_object_object_model_schema = json.loads(
    r"""{
  "type" : "object",
  "description" : "Marks that multiple events where published",
  "enum" : [ { } ]
}
""",
    object_hook=with_example_provider,
)
publish_event_response_object_object_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

publish_event_response_object_object_faker = JSF(
    publish_event_response_object_object_model_schema, allow_none_optionals=1
)


class PublishEventResponseObjectObjectStub:
    """PublishEventResponseObjectObject unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return publish_event_response_object_object_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "PublishEventResponseObjectObject":
        """Create PublishEventResponseObjectObject stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                PublishEventResponseObjectObjectAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return PublishEventResponseObjectObjectAdapter.validate_python(
            json, context={"skip_validation": True}
        )
