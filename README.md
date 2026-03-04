# Waylay Data Service
Data is ingested into the platform by the Waylay Broker.

This Python package is automatically generated based on the 
Waylay Data OpenAPI specification (API version: 2.18.0)
For more information, please visit [the openapi specification](https://docs.waylay.io/openapi/public/redocly/data.html).

It consists of two sub-packages that are both plugins for the waylay-sdk-core package.
- The `waylay-sdk-data` sub-package contains the Data api methods.
- The `waylay-sdk-data-types` sub-package is an extension that contains the typed model classes for all path params, query params, body params and responses for each of the api methods in `waylay-sdk-data`.

## Requirements.
This package requires Python 3.10+.

## Installation

Normally this package is installed together with support for other services using the [waylay-sdk](https://pypi.org/project/waylay-sdk/) umbrella package:
* `pip install waylay-sdk` will install `waylay-sdk-data` together with the SDK api packages for other services.
* `pip install waylay-sdk[types-data]` will additionally install the types package `waylay-sdk-data-types`.
* `pip install waylay-sdk[types]` will install the types packages for this and all other services.

Alternatively, you can install support for this _data_ service only, installing or extending an existing [waylay-sdk-core](https://pypi.org/project/waylay-sdk-core/):

- `pip install waylay-sdk-data` to only install api support for _data_.
- `pip install waylay-sdk-data[types]` to additionally install type support for _data_.

## Usage

```python
# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-data-types` is installed
from waylay.services.data.models.version_response import VersionResponse

try:
    # Get Service Status
    # calls `GET /data/v1/`
    api_response = await waylay_client.data.about.get()
    print(f"Response: {api_response}")
except ApiError as e:
    print("Exception when calling data.about.get: %s\n" % e)
```


For more information, please visit the [Waylay API documentation](https://docs.waylay.io/#/api/sdk/waylay-sdk/).

## Documentation for API Endpoints

All URIs are relative to *https://api.waylay.io*

SDK Path | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
**waylay_client.data.about** | [**get**](docs/AboutApi.md#get) | **GET** /data/v1/ | Get Service Status
 | | |
**waylay_client.data.events** | [**post_series**](docs/EventsApi.md#post_series) | **POST** /data/v1/events | Post Events
**waylay_client.data.events** | [**post_series_for_resource**](docs/EventsApi.md#post_series_for_resource) | **POST** /data/v1/events/{resourceId} | Post Events For Resource
**waylay_client.data.events** | [**remove**](docs/EventsApi.md#remove) | **DELETE** /data/v1/{resourceId} | Remove Data
**waylay_client.data.events** | [**stream_events**](docs/EventsApi.md#stream_events) | **GET** /data/v1/events/{resourceId} | Stream Events For Resource
 | | |
**waylay_client.data.messages** | [**delete_messages**](docs/MessagesApi.md#delete_messages) | **DELETE** /data/v1/messages/{resourceId} | Remove Messages For Resource
**waylay_client.data.messages** | [**get_latest_document**](docs/MessagesApi.md#get_latest_document) | **GET** /data/v1/messages/{resourceId}/current | Retrieve Latest Message
**waylay_client.data.messages** | [**get_latest_messages**](docs/MessagesApi.md#get_latest_messages) | **GET** /data/v1/messages/{resourceId} | Retrieve Messages For Resource
**waylay_client.data.messages** | [**query_messages**](docs/MessagesApi.md#query_messages) | **POST** /data/v1/messages/query | Query Messages
 | | |
**waylay_client.data.series** | [**delete_series**](docs/SeriesApi.md#delete_series) | **DELETE** /data/v1/series/{resourceId} | Delete Series
**waylay_client.data.series** | [**get_datapoints_for_metric_raw**](docs/SeriesApi.md#get_datapoints_for_metric_raw) | **GET** /data/v1/series/{resourceId}/{metric}/raw | Get Unaggregated Values For A Series
**waylay_client.data.series** | [**get_last_datapoints_for_metric**](docs/SeriesApi.md#get_last_datapoints_for_metric) | **GET** /data/v1/series/{resourceId}/{metric}/last | Get Last Unaggregated Values For A Series
**waylay_client.data.series** | [**get_last_metric**](docs/SeriesApi.md#get_last_metric) | **GET** /data/v1/series/{resourceId}/{metric}/latest | Get Latest Value For A Series
**waylay_client.data.series** | [**get_metric_series**](docs/SeriesApi.md#get_metric_series) | **GET** /data/v1/series/{resourceId}/{metric} | Query Series
**waylay_client.data.series** | [**get_series**](docs/SeriesApi.md#get_series) | **GET** /data/v1/series/{resourceId} | Get Series Overview
**waylay_client.data.series** | [**query_time_series**](docs/SeriesApi.md#query_time_series) | **POST** /data/v1/series/query | Query Series Data


## Documentation For Models

 - [Aggregate](docs/Aggregate.md)
 - [DeleteSeriesFromParameter](docs/DeleteSeriesFromParameter.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Event](docs/Event.md)
 - [EventTimestamp](docs/EventTimestamp.md)
 - [GetMetricSeriesFromParameter](docs/GetMetricSeriesFromParameter.md)
 - [Grouping](docs/Grouping.md)
 - [GroupingAuto](docs/GroupingAuto.md)
 - [HalLink](docs/HalLink.md)
 - [LatestMeasurement](docs/LatestMeasurement.md)
 - [LatestValue](docs/LatestValue.md)
 - [Measurements](docs/Measurements.md)
 - [MessageQuery](docs/MessageQuery.md)
 - [MessageQueryFrom](docs/MessageQueryFrom.md)
 - [MessageQueryResult](docs/MessageQueryResult.md)
 - [MessageQueryResultItem](docs/MessageQueryResultItem.md)
 - [MessageQueryUntil](docs/MessageQueryUntil.md)
 - [MessageQueryWindow](docs/MessageQueryWindow.md)
 - [MessageSuccessResult](docs/MessageSuccessResult.md)
 - [MetricSummary](docs/MetricSummary.md)
 - [ObjectData](docs/ObjectData.md)
 - [Order](docs/Order.md)
 - [PostSeriesForResourceRequest](docs/PostSeriesForResourceRequest.md)
 - [PostSeriesRequest](docs/PostSeriesRequest.md)
 - [PublishEventResponse](docs/PublishEventResponse.md)
 - [PublishEventResponseContent](docs/PublishEventResponseContent.md)
 - [PublishEventResponseObjectObject](docs/PublishEventResponseObjectObject.md)
 - [PublishResourceEventResponse](docs/PublishResourceEventResponse.md)
 - [PublishResourceEventResponseContent](docs/PublishResourceEventResponseContent.md)
 - [PublishResourceEventResponseObjectObject](docs/PublishResourceEventResponseObjectObject.md)
 - [QueryTimeSeriesRequest](docs/QueryTimeSeriesRequest.md)
 - [RawDatapointsLinks](docs/RawDatapointsLinks.md)
 - [RawDatapointsResponse](docs/RawDatapointsResponse.md)
 - [ResourceEvent](docs/ResourceEvent.md)
 - [ScalarData](docs/ScalarData.md)
 - [SeriesQueryItem](docs/SeriesQueryItem.md)
 - [SeriesQueryRequest](docs/SeriesQueryRequest.md)
 - [SeriesQueryRequestFrom](docs/SeriesQueryRequestFrom.md)
 - [SeriesQueryRequestWindow](docs/SeriesQueryRequestWindow.md)
 - [SeriesQueryResponse](docs/SeriesQueryResponse.md)
 - [SeriesQueryWithoutAggregatesRequest](docs/SeriesQueryWithoutAggregatesRequest.md)
 - [SeriesValue](docs/SeriesValue.md)
 - [TTLDuration](docs/TTLDuration.md)
 - [TimeseriesFilter](docs/TimeseriesFilter.md)
 - [TimeseriesFilterOperator](docs/TimeseriesFilterOperator.md)
 - [TimeseriesFilterOperatorOperator](docs/TimeseriesFilterOperatorOperator.md)
 - [TimeseriesFilterValue](docs/TimeseriesFilterValue.md)
 - [TimeseriesFilterValueBounds](docs/TimeseriesFilterValueBounds.md)
 - [TimeseriesFilterValueExact](docs/TimeseriesFilterValueExact.md)
 - [TimeseriesFilterValueExactValue](docs/TimeseriesFilterValueExactValue.md)
 - [TimeseriesJsonResult](docs/TimeseriesJsonResult.md)
 - [TimeseriesQueryResponse](docs/TimeseriesQueryResponse.md)
 - [TimestampedEvent](docs/TimestampedEvent.md)
 - [TimestampedResourceEvent](docs/TimestampedResourceEvent.md)
 - [VersionResponse](docs/VersionResponse.md)

