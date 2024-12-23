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
    from waylay.services.data.models.timeseries_filter_operator_operator import (
        TimeseriesFilterOperatorOperator,
    )

    TimeseriesFilterOperatorOperatorAdapter = TypeAdapter(
        TimeseriesFilterOperatorOperator
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

timeseries_filter_operator_operator_model_schema = json.loads(
    r"""{
  "title" : "TimeseriesFilterOperator_operator",
  "type" : "string",
  "enum" : [ "gt", "gte", "lt", "lte", "eq", "ne", "between" ]
}
""",
    object_hook=with_example_provider,
)
timeseries_filter_operator_operator_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

timeseries_filter_operator_operator_faker = JSF(
    timeseries_filter_operator_operator_model_schema, allow_none_optionals=1
)


class TimeseriesFilterOperatorOperatorStub:
    """TimeseriesFilterOperatorOperator unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return timeseries_filter_operator_operator_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "TimeseriesFilterOperatorOperator":
        """Create TimeseriesFilterOperatorOperator stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TimeseriesFilterOperatorOperatorAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TimeseriesFilterOperatorOperatorAdapter.validate_python(
            json, context={"skip_validation": True}
        )
