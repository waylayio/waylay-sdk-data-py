# coding: utf-8
"""Waylay Broker: Service.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

version: 2.14.0

Data is ingested into the platform by the Waylay Broker.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

__version__ = "2.14.0.20240327"

from .service import DataService

PLUGINS = [DataService]

__all__ = [
    "__version__",
    "DataService",
]
