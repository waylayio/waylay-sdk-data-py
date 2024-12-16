# Waylay Data Service
Data is ingested into the platform by the Waylay Broker.

This Python package is automatically generated based on the 
Waylay Data OpenAPI specification (API version: 2.18.0)
For more information, please visit [the openapi specification](https://docs.waylay.io/openapi/public/redocly/data.html).

It consists of two sub-packages that are both plugins for the waylay-sdk-core package.
- The `waylay-sdk-data` sub-package contains the Data api methods.
- The `waylay-sdk-data-types` sub-package is an extension that contains the typed model classes for all path params, query params, body params and responses for each of the api methods in `waylay-sdk-data`.

## Requirements.
This package requires Python 3.9+.

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
from pprint import pprint

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
    api_response = await waylay_client.data.about.get(
    )
    print("The response of data.about.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.about.get: %s\n" % e)
```


For more information, please visit the [Waylay API documentation](https://docs.waylay.io/#/api/?id=software-development-kits).

## Documentation for API Endpoints

All URIs are relative to *https://api.waylay.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AboutApi* | [**get**](docs/AboutApi.md#get) | **GET** /data/v1/ | Get Service Status
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


## Documentation For Models

 - [Aggregate](docs/Aggregate.md)
 - [DeleteMessages200Response](docs/DeleteMessages200Response.md)
 - [DeleteSeriesFromParameter](docs/DeleteSeriesFromParameter.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Event](docs/Event.md)
 - [EventTimestamp](docs/EventTimestamp.md)
 - [GetDatapointsForMetricRaw200Response](docs/GetDatapointsForMetricRaw200Response.md)
 - [GetDatapointsForMetricRaw200ResponseLinks](docs/GetDatapointsForMetricRaw200ResponseLinks.md)
 - [GetMetricSeriesFromParameter](docs/GetMetricSeriesFromParameter.md)
 - [GetSeries200ResponseInner](docs/GetSeries200ResponseInner.md)
 - [GetSeries200ResponseInnerLatest](docs/GetSeries200ResponseInnerLatest.md)
 - [Grouping](docs/Grouping.md)
 - [GroupingAnyOf](docs/GroupingAnyOf.md)
 - [HalLink](docs/HalLink.md)
 - [LatestMeasurement](docs/LatestMeasurement.md)
 - [Measurements](docs/Measurements.md)
 - [MessageQuery](docs/MessageQuery.md)
 - [MessageQueryFrom](docs/MessageQueryFrom.md)
 - [MessageQueryResult](docs/MessageQueryResult.md)
 - [MessageQueryResultResultsInner](docs/MessageQueryResultResultsInner.md)
 - [MessageQueryUntil](docs/MessageQueryUntil.md)
 - [MessageQueryWindow](docs/MessageQueryWindow.md)
 - [MultipleSeriesQueryRequestInner](docs/MultipleSeriesQueryRequestInner.md)
 - [ObjectData](docs/ObjectData.md)
 - [Order](docs/Order.md)
 - [PostSeriesForResourceRequest](docs/PostSeriesForResourceRequest.md)
 - [PostSeriesRequest](docs/PostSeriesRequest.md)
 - [PublishEventResponse](docs/PublishEventResponse.md)
 - [PublishEventResponseContent](docs/PublishEventResponseContent.md)
 - [PublishEventResponseContentAnyOf](docs/PublishEventResponseContentAnyOf.md)
 - [PublishResourceEventResponse](docs/PublishResourceEventResponse.md)
 - [PublishResourceEventResponseContent](docs/PublishResourceEventResponseContent.md)
 - [QueryTimeSeries200Response](docs/QueryTimeSeries200Response.md)
 - [QueryTimeSeriesRequest](docs/QueryTimeSeriesRequest.md)
 - [ResourceEvent](docs/ResourceEvent.md)
 - [ScalarData](docs/ScalarData.md)
 - [SeriesKeyValueInner](docs/SeriesKeyValueInner.md)
 - [SeriesQueryRequest](docs/SeriesQueryRequest.md)
 - [SeriesQueryRequestFrom](docs/SeriesQueryRequestFrom.md)
 - [SeriesQueryRequestWindow](docs/SeriesQueryRequestWindow.md)
 - [SeriesQueryResponse](docs/SeriesQueryResponse.md)
 - [SeriesQueryWithoutAggregatesRequest](docs/SeriesQueryWithoutAggregatesRequest.md)
 - [TTLDuration](docs/TTLDuration.md)
 - [TimeseriesFilter](docs/TimeseriesFilter.md)
 - [TimeseriesFilterOperator](docs/TimeseriesFilterOperator.md)
 - [TimeseriesFilterOperatorOperator](docs/TimeseriesFilterOperatorOperator.md)
 - [TimeseriesFilterValue](docs/TimeseriesFilterValue.md)
 - [TimeseriesFilterValueBounds](docs/TimeseriesFilterValueBounds.md)
 - [TimeseriesFilterValueExact](docs/TimeseriesFilterValueExact.md)
 - [TimeseriesFilterValueExactValue](docs/TimeseriesFilterValueExactValue.md)
 - [TimeseriesJsonResult](docs/TimeseriesJsonResult.md)
 - [TimestampedEvent](docs/TimestampedEvent.md)
 - [TimestampedResourceEvent](docs/TimestampedResourceEvent.md)
 - [VersionResponse](docs/VersionResponse.md)

