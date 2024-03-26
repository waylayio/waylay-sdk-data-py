# Waylay Data Service
Data is ingested into the platform by the Waylay Broker.

This Python package is automatically generated based on the 
Waylay Data OpenAPI specification (API version: 2.14.0)

It consists of a plugin for the waylay-sdk package, and contains the Data api methods.
Note that the typed model classes for all path params, query params, body params and responses for each of the api methods are contained in a separate package called waylay-sdk-data-types.

## Requirements.
This package requires Python 3.9+.

## Installation
Typically this package is installed when installing the [waylay-sdk](https://github.com/waylayio/waylay-sdk-py) package to enable the service's functionality.
When the service api methods are required, waylay-sdk-data is included in:
- ```pip install waylay-sdk[data]``` to install `waylay-sdk` along with only this service, or
- ```pip install waylay-sdk[services]``` to install `waylay-sdk` along with all services.
When the typed models are required, both waylay-sdk-data and waylay-sdk-data-types are included in:
- ```pip install waylay-sdk[data,data-types]``` to install `waylay-sdk` along with only this service including the typed models, or
- ```pip install waylay-sdk[services,services-types]``` to install `waylay-sdk` along with all services along with the typed models.

## Usage


```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Model classes for responses/parameters are available only when `waylay-sdk-data-types` is installed
from data.models.timestamped_resource_event import TimestampedResourceEvent
try:
    # Stream Events For Resource
    # calls `GET /data/v1/events/{resourceId}`
    api_response = await waylay_client.data.events.stream_events(
        'resource_id_example', # resource_id | path param "resourceId"
    )
    print("The response of data.events.stream_events:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.events.stream_events: %s\n" % e)
```


## Documentation for API Endpoints

All URIs are relative to *https://api.waylay.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EventsApi* | [**post_series**](docs/EventsApi.md#post_series) | **POST** /data/v1/events | Post Events
*EventsApi* | [**post_series_for_resource**](docs/EventsApi.md#post_series_for_resource) | **POST** /data/v1/events/{resourceId} | Post Events For Resource
*EventsApi* | [**remove**](docs/EventsApi.md#remove) | **DELETE** /data/v1/{resourceId} | Remove Data
*EventsApi* | [**stream_events**](docs/EventsApi.md#stream_events) | **GET** /data/v1/events/{resourceId} | Stream Events For Resource
*MessagesApi* | [**delete_messages**](docs/MessagesApi.md#delete_messages) | **DELETE** /data/v1/messages/{resourceId} | Remove Messages For Resource
*MessagesApi* | [**get_latest_document**](docs/MessagesApi.md#get_latest_document) | **GET** /data/v1/messages/{resourceId}/current | Retrieve Latest Message
*MessagesApi* | [**get_latest_messages**](docs/MessagesApi.md#get_latest_messages) | **GET** /data/v1/messages/{resourceId} | Retrieve Messages For Resource
*MessagesApi* | [**query_messages**](docs/MessagesApi.md#query_messages) | **POST** /data/v1/messages/query | Query Messages
*SeriesApi* | [**delete_series**](docs/SeriesApi.md#delete_series) | **DELETE** /data/v1/series/{resourceId} | Delete Series
*SeriesApi* | [**get_datapoints_for_metric_raw**](docs/SeriesApi.md#get_datapoints_for_metric_raw) | **GET** /data/v1/series/{resourceId}/{metric}/raw | Get Unaggregated Values For A Series
*SeriesApi* | [**get_last_datapoints_for_metric**](docs/SeriesApi.md#get_last_datapoints_for_metric) | **GET** /data/v1/series/{resourceId}/{metric}/last | Get Last Unaggregated Values For A Series
*SeriesApi* | [**get_last_metric**](docs/SeriesApi.md#get_last_metric) | **GET** /data/v1/series/{resourceId}/{metric}/latest | Get Latest Value For A Series
*SeriesApi* | [**get_metric_series**](docs/SeriesApi.md#get_metric_series) | **GET** /data/v1/series/{resourceId}/{metric} | Query Series
*SeriesApi* | [**get_series**](docs/SeriesApi.md#get_series) | **GET** /data/v1/series/{resourceId} | Get Series Overview
*SeriesApi* | [**query_time_series**](docs/SeriesApi.md#query_time_series) | **POST** /data/v1/series/query | Query Series Data
*VersionApi* | [**health**](docs/VersionApi.md#health) | **GET** /data/v1/ | Version


