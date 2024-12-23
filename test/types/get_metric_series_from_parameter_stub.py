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
    from waylay.services.data.models.get_metric_series_from_parameter import (
        GetMetricSeriesFromParameter,
    )

    GetMetricSeriesFromParameterAdapter = TypeAdapter(GetMetricSeriesFromParameter)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

get_metric_series_from_parameter_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/SO8601Timestamp"
  } ]
}
""",
    object_hook=with_example_provider,
)
get_metric_series_from_parameter_model_schema.update({"definitions": MODEL_DEFINITIONS})

get_metric_series_from_parameter_faker = JSF(
    get_metric_series_from_parameter_model_schema, allow_none_optionals=1
)


class GetMetricSeriesFromParameterStub:
    """GetMetricSeriesFromParameter unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_metric_series_from_parameter_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "GetMetricSeriesFromParameter":
        """Create GetMetricSeriesFromParameter stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GetMetricSeriesFromParameterAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GetMetricSeriesFromParameterAdapter.validate_python(
            json, context={"skip_validation": True}
        )
