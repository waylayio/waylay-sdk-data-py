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
    from waylay.services.data.models.timeseries_filter_value import (
        TimeseriesFilterValue,
    )

    TimeseriesFilterValueAdapter = TypeAdapter(TimeseriesFilterValue)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

timeseries_filter_value_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/TimeseriesFilterValueExact"
  }, {
    "$ref" : "#/components/schemas/TimeseriesFilterValueBounds"
  } ]
}
""",
    object_hook=with_example_provider,
)
timeseries_filter_value_model_schema.update({"definitions": MODEL_DEFINITIONS})

timeseries_filter_value_faker = JSF(
    timeseries_filter_value_model_schema, allow_none_optionals=1
)


class TimeseriesFilterValueStub:
    """TimeseriesFilterValue unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return timeseries_filter_value_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "TimeseriesFilterValue":
        """Create TimeseriesFilterValue stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TimeseriesFilterValueAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TimeseriesFilterValueAdapter.validate_python(
            json, context={"skip_validation": True}
        )
