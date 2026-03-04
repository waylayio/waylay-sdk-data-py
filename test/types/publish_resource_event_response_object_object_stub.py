"""Waylay Broker model tests.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.data.models.publish_resource_event_response_object_object import (
        PublishResourceEventResponseObjectObject,
    )

    PublishResourceEventResponseObjectObjectAdapter = TypeAdapter(
        PublishResourceEventResponseObjectObject
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

publish_resource_event_response_object_object_model_schema = json.loads(
    r"""{
  "type" : "object",
  "description" : "Marks that multiple events where published",
  "enum" : [ { } ]
}
""",
    object_hook=with_example_provider,
)
publish_resource_event_response_object_object_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

publish_resource_event_response_object_object_faker = JSF(
    publish_resource_event_response_object_object_model_schema, allow_none_optionals=1
)


class PublishResourceEventResponseObjectObjectStub:
    """PublishResourceEventResponseObjectObject unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return publish_resource_event_response_object_object_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "PublishResourceEventResponseObjectObject":
        """Create PublishResourceEventResponseObjectObject stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                PublishResourceEventResponseObjectObjectAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return PublishResourceEventResponseObjectObjectAdapter.validate_python(
            json, context={"skip_validation": True}
        )
