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
    from waylay.services.data.models.scalar_data import ScalarData

    ScalarDataAdapter = TypeAdapter(ScalarData)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

scalar_data_model_schema = json.loads(
    r"""{
  "title" : "ScalarData",
  "description" : "Event data stored in both the _Message Cache_ and _Time Series Database_.\nKeys of these measurements become a _Metric_ for the resource.",
  "nullable" : true,
  "oneOf" : [ {
    "title" : "Number",
    "type" : "number"
  }, {
    "title" : "String",
    "type" : "string"
  }, {
    "title" : "Boolean",
    "type" : "boolean"
  } ]
}
""",
    object_hook=with_example_provider,
)
scalar_data_model_schema.update({"definitions": MODEL_DEFINITIONS})

scalar_data_faker = JSF(scalar_data_model_schema, allow_none_optionals=1)


class ScalarDataStub:
    """ScalarData unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return scalar_data_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ScalarData":
        """Create ScalarData stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(ScalarDataAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ScalarDataAdapter.validate_python(
            json, context={"skip_validation": True}
        )
