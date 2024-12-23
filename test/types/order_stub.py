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
    from waylay.services.data.models.order import Order

    OrderAdapter = TypeAdapter(Order)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

order_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "the order in which the data is returned",
  "default" : "ascending",
  "enum" : [ "ascending", "descending" ]
}
""",
    object_hook=with_example_provider,
)
order_model_schema.update({"definitions": MODEL_DEFINITIONS})

order_faker = JSF(order_model_schema, allow_none_optionals=1)


class OrderStub:
    """Order unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return order_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Order":
        """Create Order stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(OrderAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return OrderAdapter.validate_python(json, context={"skip_validation": True})
