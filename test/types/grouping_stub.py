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
    from waylay.services.data.models.grouping import Grouping

    GroupingAdapter = TypeAdapter(Grouping)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

grouping_model_schema = json.loads(
    r"""{
  "externalDocs" : {
    "description" : "Possible groupings",
    "url" : "https://docs.waylay.io/#/api/broker/?id=grouping"
  },
  "anyOf" : [ {
    "$ref" : "#/components/schemas/auto"
  }, {
    "$ref" : "#/components/schemas/DurationWithUnit"
  }, {
    "$ref" : "#/components/schemas/SO8601Duration"
  } ]
}
""",
    object_hook=with_example_provider,
)
grouping_model_schema.update({"definitions": MODEL_DEFINITIONS})

grouping_faker = JSF(grouping_model_schema, allow_none_optionals=1)


class GroupingStub:
    """Grouping unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return grouping_faker.generate()

    @classmethod
    def create_instance(cls) -> "Grouping":
        """Create Grouping stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return GroupingAdapter.validate_python(cls.create_json())
