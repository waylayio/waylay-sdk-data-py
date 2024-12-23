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
    from waylay.services.data.models.publish_event_response_content_any_of import (
        PublishEventResponseContentAnyOf,
    )

    PublishEventResponseContentAnyOfAdapter = TypeAdapter(
        PublishEventResponseContentAnyOf
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

publish_event_response_content_any_of_model_schema = json.loads(
    r"""{
  "type" : "object",
  "description" : "Marks that multiple events where published",
  "enum" : [ { } ]
}
""",
    object_hook=with_example_provider,
)
publish_event_response_content_any_of_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

publish_event_response_content_any_of_faker = JSF(
    publish_event_response_content_any_of_model_schema, allow_none_optionals=1
)


class PublishEventResponseContentAnyOfStub:
    """PublishEventResponseContentAnyOf unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return publish_event_response_content_any_of_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "PublishEventResponseContentAnyOf":
        """Create PublishEventResponseContentAnyOf stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                PublishEventResponseContentAnyOfAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return PublishEventResponseContentAnyOfAdapter.validate_python(
            json, context={"skip_validation": True}
        )
