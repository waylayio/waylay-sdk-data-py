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
    from waylay.services.data.models.post_series_for_resource_request import (
        PostSeriesForResourceRequest,
    )

    PostSeriesForResourceRequestAdapter = TypeAdapter(PostSeriesForResourceRequest)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

post_series_for_resource_request_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/Event"
  }, {
    "$ref" : "#/components/schemas/Events"
  } ]
}
""",
    object_hook=with_example_provider,
)
post_series_for_resource_request_model_schema.update({"definitions": MODEL_DEFINITIONS})

post_series_for_resource_request_faker = JSF(
    post_series_for_resource_request_model_schema, allow_none_optionals=1
)


class PostSeriesForResourceRequestStub:
    """PostSeriesForResourceRequest unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return { "timestamp": 1729869037000, "temperature": 23 }

    @classmethod
    def create_instance(cls) -> "PostSeriesForResourceRequest":
        """Create PostSeriesForResourceRequest stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                PostSeriesForResourceRequestAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return PostSeriesForResourceRequestAdapter.validate_python(
            json, context={"skip_validation": True}
        )
