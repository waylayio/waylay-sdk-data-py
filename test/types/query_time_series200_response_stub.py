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
    from waylay.services.data.models.query_time_series200_response import (
        QueryTimeSeries200Response,
    )

    QueryTimeSeries200ResponseAdapter = TypeAdapter(QueryTimeSeries200Response)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

query_time_series_200_response_model_schema = json.loads(
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
query_time_series_200_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

query_time_series_200_response_faker = JSF(
    query_time_series_200_response_model_schema, allow_none_optionals=1
)


class QueryTimeSeries200ResponseStub:
    """QueryTimeSeries200Response unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return query_time_series_200_response_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "QueryTimeSeries200Response":
        """Create QueryTimeSeries200Response stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                QueryTimeSeries200ResponseAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return QueryTimeSeries200ResponseAdapter.validate_python(
            json, context={"skip_validation": True}
        )
