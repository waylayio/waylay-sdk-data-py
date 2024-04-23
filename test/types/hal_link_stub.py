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
    from waylay.services.data.models.hal_link import HalLink

    HalLinkAdapter = TypeAdapter(HalLink)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

hal_link_model_schema = json.loads(
    r"""{
  "required" : [ "href", "name" ],
  "type" : "object",
  "properties" : {
    "href" : {
      "type" : "string",
      "format" : "url",
      "example" : "/series/test1/a/raw?from=1663269720694&until=1665833921682&order=ascending"
    },
    "name" : {
      "type" : "string",
      "example" : "Next series"
    }
  }
}
""",
    object_hook=with_example_provider,
)
hal_link_model_schema.update({"definitions": MODEL_DEFINITIONS})

hal_link_faker = JSF(hal_link_model_schema, allow_none_optionals=1)


class HalLinkStub:
    """HalLink unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return hal_link_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "HalLink":
        """Create HalLink stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(HalLinkAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return HalLinkAdapter.validate_python(json, context={"skip_validation": True})
