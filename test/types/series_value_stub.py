"""Waylay Broker model tests.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.data.models.series_value import SeriesValue

    SeriesValueAdapter = TypeAdapter(SeriesValue)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

series_value_model_schema = json.loads(
    r"""{
  "title" : "SeriesValue",
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
series_value_model_schema.update({"definitions": MODEL_DEFINITIONS})

series_value_faker = JSF(series_value_model_schema, allow_none_optionals=1)


class SeriesValueStub:
    """SeriesValue unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return series_value_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "SeriesValue":
        """Create SeriesValue stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(SeriesValueAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SeriesValueAdapter.validate_python(
            json, context={"skip_validation": True}
        )
