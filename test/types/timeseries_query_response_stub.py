"""Waylay Broker model tests.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.data.models.timeseries_query_response import (
        TimeseriesQueryResponse,
    )

    TimeseriesQueryResponseAdapter = TypeAdapter(TimeseriesQueryResponse)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

timeseries_query_response_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/TimeseriesJsonResult"
  }, {
    "$ref" : "#/components/schemas/MultipleTimeseriesJsonResult"
  } ]
}
""",
    object_hook=with_example_provider,
)
timeseries_query_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

timeseries_query_response_faker = JSF(
    timeseries_query_response_model_schema, allow_none_optionals=1
)


class TimeseriesQueryResponseStub:
    """TimeseriesQueryResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return timeseries_query_response_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "TimeseriesQueryResponse":
        """Create TimeseriesQueryResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TimeseriesQueryResponseAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TimeseriesQueryResponseAdapter.validate_python(
            json, context={"skip_validation": True}
        )
