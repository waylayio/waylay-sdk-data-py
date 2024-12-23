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
    from waylay.services.data.models.measurements import Measurements

    MeasurementsAdapter = TypeAdapter(Measurements)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

measurements_model_schema = json.loads(
    r"""{
  "title" : "Measurements",
  "description" : "Values in an _Event_ payload.\nNote that only _scalar_ data is stored in the timeseries, while\nArrays and objects are only stored in the _Message Cache_.",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/ScalarData"
  }, {
    "$ref" : "#/components/schemas/Object_Data"
  } ]
}
""",
    object_hook=with_example_provider,
)
measurements_model_schema.update({"definitions": MODEL_DEFINITIONS})

measurements_faker = JSF(measurements_model_schema, allow_none_optionals=1)


class MeasurementsStub:
    """Measurements unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return measurements_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Measurements":
        """Create Measurements stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                MeasurementsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return MeasurementsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
