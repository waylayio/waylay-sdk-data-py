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
    from waylay.services.data.models.series_key_value_inner import SeriesKeyValueInner

    SeriesKeyValueInnerAdapter = TypeAdapter(SeriesKeyValueInner)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

series_key_value_inner_model_schema = json.loads(
    r"""{
  "title" : "SeriesKeyValue_inner",
  "nullable" : true,
  "oneOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/ScalarData"
  } ]
}
""",
    object_hook=with_example_provider,
)
series_key_value_inner_model_schema.update({"definitions": MODEL_DEFINITIONS})

series_key_value_inner_faker = JSF(
    series_key_value_inner_model_schema, allow_none_optionals=1
)


class SeriesKeyValueInnerStub:
    """SeriesKeyValueInner unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return series_key_value_inner_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "SeriesKeyValueInner":
        """Create SeriesKeyValueInner stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SeriesKeyValueInnerAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SeriesKeyValueInnerAdapter.validate_python(
            json, context={"skip_validation": True}
        )
