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
    from waylay.services.data.models.aggregate import Aggregate

    AggregateAdapter = TypeAdapter(Aggregate)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

aggregate_model_schema = json.loads(
    r"""{
  "type" : "string",
  "example" : "mean",
  "externalDocs" : {
    "description" : "Possible functions",
    "url" : "https://docs.waylay.io/#/api/broker/?id=aggregates"
  },
  "enum" : [ "min", "max", "mean", "median", "sum", "count", "count-non-numeric", "count-numeric", "first", "last", "std", "diff" ]
}
""",
    object_hook=with_example_provider,
)
aggregate_model_schema.update({"definitions": MODEL_DEFINITIONS})

aggregate_faker = JSF(aggregate_model_schema, allow_none_optionals=1)


class AggregateStub:
    """Aggregate unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return aggregate_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Aggregate":
        """Create Aggregate stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(AggregateAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AggregateAdapter.validate_python(json, context={"skip_validation": True})
