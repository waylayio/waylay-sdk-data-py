"""Waylay Broker model tests.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.data.models.grouping_auto import GroupingAuto

    GroupingAutoAdapter = TypeAdapter(GroupingAuto)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

grouping_auto_model_schema = json.loads(
    r"""{
  "title" : "GroupingAuto",
  "type" : "string",
  "enum" : [ "auto" ]
}
""",
    object_hook=with_example_provider,
)
grouping_auto_model_schema.update({"definitions": MODEL_DEFINITIONS})

grouping_auto_faker = JSF(grouping_auto_model_schema, allow_none_optionals=1)


class GroupingAutoStub:
    """GroupingAuto unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return grouping_auto_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "GroupingAuto":
        """Create GroupingAuto stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GroupingAutoAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GroupingAutoAdapter.validate_python(
            json, context={"skip_validation": True}
        )
