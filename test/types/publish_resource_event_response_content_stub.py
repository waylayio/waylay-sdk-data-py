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
    from waylay.services.data.models.publish_resource_event_response_content import (
        PublishResourceEventResponseContent,
    )

    PublishResourceEventResponseContentAdapter = TypeAdapter(
        PublishResourceEventResponseContent
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

publish_resource_event_response_content_model_schema = json.loads(
    r"""{
  "title" : "PublishResourceEventResponse_content",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/TimestampedEvent"
  }, {
    "$ref" : "#/components/schemas/PublishEventResponse_content_anyOf"
  } ]
}
""",
    object_hook=with_example_provider,
)
publish_resource_event_response_content_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

publish_resource_event_response_content_faker = JSF(
    publish_resource_event_response_content_model_schema, allow_none_optionals=1
)


class PublishResourceEventResponseContentStub:
    """PublishResourceEventResponseContent unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return publish_resource_event_response_content_faker.generate()

    @classmethod
    def create_instance(cls) -> "PublishResourceEventResponseContent":
        """Create PublishResourceEventResponseContent stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return PublishResourceEventResponseContentAdapter.validate_python(
            cls.create_json()
        )
