# waylay.services.data.SeriesApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_series**](SeriesApi.md#delete_series) | **DELETE** /data/v1/series/{resourceId} | Delete Series
[**get_datapoints_for_metric_raw**](SeriesApi.md#get_datapoints_for_metric_raw) | **GET** /data/v1/series/{resourceId}/{metric}/raw | Get Unaggregated Values For A Series
[**get_last_datapoints_for_metric**](SeriesApi.md#get_last_datapoints_for_metric) | **GET** /data/v1/series/{resourceId}/{metric}/last | Get Last Unaggregated Values For A Series
[**get_last_metric**](SeriesApi.md#get_last_metric) | **GET** /data/v1/series/{resourceId}/{metric}/latest | Get Latest Value For A Series
[**get_metric_series**](SeriesApi.md#get_metric_series) | **GET** /data/v1/series/{resourceId}/{metric} | Query Series
[**get_series**](SeriesApi.md#get_series) | **GET** /data/v1/series/{resourceId} | Get Series Overview
[**query_time_series**](SeriesApi.md#query_time_series) | **POST** /data/v1/series/query | Query Series Data

# **delete_series**
> delete_series(
> resource_id: str,
> query: DeleteSeriesQuery,
> headers
> ) -> DeleteMessages200Response

Delete Series

Removes all timeseries associated with a resource.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-data-types` is installed
from waylay.services.data.models.delete_messages200_response import DeleteMessages200Response
try:
    # Delete Series
    # calls `DELETE /data/v1/series/{resourceId}`
    api_response = await waylay_client.data.series.delete_series(
        'resource_id_example', # resource_id | path param "resourceId"
        # query parameters:
        query = {
        },
    )
    print("The response of data.series.delete_series:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.series.delete_series: %s\n" % e)
```

### Endpoint
```
DELETE /data/v1/series/{resourceId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **str** | path parameter `"resourceId"` | Uniquely identifies a resource. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['from']** (dict) <br> **query.var_from** (Query) | [**DeleteSeriesFromParameter**](.md) | query parameter `"from"` | Specifies the lower bound of the time period | [optional] 
**query['until']** (dict) <br> **query.until** (Query) | [**DeleteSeriesFromParameter**](.md) | query parameter `"until"` | Specifies the upper bound of the time period | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`DeleteMessages200Response`** |  | [DeleteMessages200Response](DeleteMessages200Response.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datapoints_for_metric_raw**
> get_datapoints_for_metric_raw(
> resource_id: str,
> metric: str,
> query: GetDatapointsForMetricRawQuery,
> headers
> ) -> TimeseriesJsonResult

Get Unaggregated Values For A Series

Retrieves the raw, unaggregated values for a series.  When a request with content type `application/hal+json` leads to more datapoints in the requested interval than the `limit` parameter allows, then the response contains a HAL `_links.next` url that resolves to a  next batch of datapoints.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-data-types` is installed
from waylay.services.data.models.order import Order
from waylay.services.data.models.timeseries_json_result import TimeseriesJsonResult
try:
    # Get Unaggregated Values For A Series
    # calls `GET /data/v1/series/{resourceId}/{metric}/raw`
    api_response = await waylay_client.data.series.get_datapoints_for_metric_raw(
        'resource_id_example', # resource_id | path param "resourceId"
        'metric_example', # metric | path param "metric"
        # query parameters:
        query = {
        },
    )
    print("The response of data.series.get_datapoints_for_metric_raw:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.series.get_datapoints_for_metric_raw: %s\n" % e)
```

### Endpoint
```
GET /data/v1/series/{resourceId}/{metric}/raw
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **str** | path parameter `"resourceId"` | Uniquely identifies a resource. | 
**metric** | **str** | path parameter `"metric"` | Identifies the times series metric. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['from']** (dict) <br> **query.var_from** (Query) | [**GetMetricSeriesFromParameter**](.md) | query parameter `"from"` | Specifies the lower bound of the time period. If not specified, a period of 7 days before &#x60;until&#x60; (or before the request was received) will be queried. | [optional] 
**query['until']** (dict) <br> **query.until** (Query) | [**GetMetricSeriesFromParameter**](.md) | query parameter `"until"` | Specifies the upper bound of the time period. If not specified, a period of 7 days after &#x60;from&#x60; (or before the request was received) will be queried | [optional] 
**query['limit']** (dict) <br> **query.limit** (Query) | **int** | query parameter `"limit"` | max number of values to retrieve | [optional] [default 1]
**query['order']** (dict) <br> **query.order** (Query) | [**Order**](.md) | query parameter `"order"` | sort order | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TimeseriesJsonResult`** |  | [TimeseriesJsonResult](TimeseriesJsonResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_datapoints_for_metric**
> get_last_datapoints_for_metric(
> resource_id: str,
> metric: str,
> query: GetLastDatapointsForMetricQuery,
> headers
> ) -> TimeseriesJsonResult

Get Last Unaggregated Values For A Series

Query the time series storage for the latest n datapoints for a particular metric from a resource.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-data-types` is installed
from waylay.services.data.models.timeseries_json_result import TimeseriesJsonResult
try:
    # Get Last Unaggregated Values For A Series
    # calls `GET /data/v1/series/{resourceId}/{metric}/last`
    api_response = await waylay_client.data.series.get_last_datapoints_for_metric(
        'resource_id_example', # resource_id | path param "resourceId"
        'metric_example', # metric | path param "metric"
        # query parameters:
        query = {
        },
    )
    print("The response of data.series.get_last_datapoints_for_metric:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.series.get_last_datapoints_for_metric: %s\n" % e)
```

### Endpoint
```
GET /data/v1/series/{resourceId}/{metric}/last
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **str** | path parameter `"resourceId"` | Uniquely identifies a resource. | 
**metric** | **str** | path parameter `"metric"` | Identifies the times series metric. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['limit']** (dict) <br> **query.limit** (Query) | **int** | query parameter `"limit"` | max number of values to retrieve | [optional] [default 1]
**query['until']** (dict) <br> **query.until** (Query) | [**GetMetricSeriesFromParameter**](.md) | query parameter `"until"` | Specifies the upper bound of the time period. If not specified, a period of 7 days after &#x60;from&#x60; (or before the request was received) will be queried | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TimeseriesJsonResult`** |  | [TimeseriesJsonResult](TimeseriesJsonResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_metric**
> get_last_metric(
> resource_id: str,
> metric: str,
> headers
> ) -> LatestMeasurement

Get Latest Value For A Series

Retrieves the latest value of a time series.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-data-types` is installed
from waylay.services.data.models.latest_measurement import LatestMeasurement
try:
    # Get Latest Value For A Series
    # calls `GET /data/v1/series/{resourceId}/{metric}/latest`
    api_response = await waylay_client.data.series.get_last_metric(
        'resource_id_example', # resource_id | path param "resourceId"
        'metric_example', # metric | path param "metric"
    )
    print("The response of data.series.get_last_metric:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.series.get_last_metric: %s\n" % e)
```

### Endpoint
```
GET /data/v1/series/{resourceId}/{metric}/latest
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **str** | path parameter `"resourceId"` | Uniquely identifies a resource. | 
**metric** | **str** | path parameter `"metric"` | Identifies the times series metric. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`LatestMeasurement`** |  | [LatestMeasurement](LatestMeasurement.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | No Data Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metric_series**
> get_metric_series(
> resource_id: str,
> metric: str,
> query: GetMetricSeriesQuery,
> headers
> ) -> TimeseriesJsonResult

Query Series

Queries a single timeseries. Depending on the `grouping` query parameter, data will be aggregated (if `grouping` is specified) or not. If data will be aggregated, you must specify one (through `aggregate` parameter) or more (through `aggregates` parameter) aggregation function(s).Optional order parameter applies sorting order to the result.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-data-types` is installed
from waylay.services.data.models.aggregate import Aggregate
from waylay.services.data.models.order import Order
from waylay.services.data.models.timeseries_json_result import TimeseriesJsonResult
try:
    # Query Series
    # calls `GET /data/v1/series/{resourceId}/{metric}`
    api_response = await waylay_client.data.series.get_metric_series(
        'resource_id_example', # resource_id | path param "resourceId"
        'metric_example', # metric | path param "metric"
        # query parameters:
        query = {
        },
    )
    print("The response of data.series.get_metric_series:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.series.get_metric_series: %s\n" % e)
```

### Endpoint
```
GET /data/v1/series/{resourceId}/{metric}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **str** | path parameter `"resourceId"` | Uniquely identifies a resource. | 
**metric** | **str** | path parameter `"metric"` | Identifies the times series metric. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['from']** (dict) <br> **query.var_from** (Query) | [**GetMetricSeriesFromParameter**](.md) | query parameter `"from"` | Specifies the lower bound of the time period. If not specified, a period of 7 days before &#x60;until&#x60; (or before the request was received) will be queried. | [optional] 
**query['until']** (dict) <br> **query.until** (Query) | [**GetMetricSeriesFromParameter**](.md) | query parameter `"until"` | Specifies the upper bound of the time period. If not specified, a period of 7 days after &#x60;from&#x60; (or before the request was received) will be queried | [optional] 
**query['aggregate']** (dict) <br> **query.aggregate** (Query) | [**Aggregate**](.md) | query parameter `"aggregate"` | Specifies the aggregation function to use | [optional] 
**query['aggregates']** (dict) <br> **query.aggregates** (Query) | **str** | query parameter `"aggregates"` | comma-separated list of aggregation functions | [optional] 
**query['grouping']** (dict) <br> **query.grouping** (Query) | [**Grouping**](.md) | query parameter `"grouping"` | time period over which timeseries data must be aggregates | [optional] 
**query['order']** (dict) <br> **query.order** (Query) | [**Order**](.md) | query parameter `"order"` | sort order | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TimeseriesJsonResult`** |  | [TimeseriesJsonResult](TimeseriesJsonResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_series**
> get_series(
> resource_id: str,
> headers
> ) -> List[GetSeries200ResponseInner]

Get Series Overview

Lists the existing timeseries for the given resource.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-data-types` is installed
from waylay.services.data.models.get_series200_response_inner import GetSeries200ResponseInner
try:
    # Get Series Overview
    # calls `GET /data/v1/series/{resourceId}`
    api_response = await waylay_client.data.series.get_series(
        'resource_id_example', # resource_id | path param "resourceId"
    )
    print("The response of data.series.get_series:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.series.get_series: %s\n" % e)
```

### Endpoint
```
GET /data/v1/series/{resourceId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **str** | path parameter `"resourceId"` | Uniquely identifies a resource. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`List[GetSeries200ResponseInner]`** |  | [List[GetSeries200ResponseInner]](GetSeries200ResponseInner.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_time_series**
> query_time_series(
> headers
> ) -> QueryTimeSeries200Response

Query Series Data

Executes an ad-hoc timeseries query.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-data-types` is installed
from waylay.services.data.models.query_time_series200_response import QueryTimeSeries200Response
from waylay.services.data.models.query_time_series_request import QueryTimeSeriesRequest
try:
    # Query Series Data
    # calls `POST /data/v1/series/query`
    api_response = await waylay_client.data.series.query_time_series(
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.data.QueryTimeSeriesRequest() # QueryTimeSeriesRequest | 
    )
    print("The response of data.series.query_time_series:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.series.query_time_series: %s\n" % e)
```

### Endpoint
```
POST /data/v1/series/query
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**QueryTimeSeriesRequest**](QueryTimeSeriesRequest.md) | json request body |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`QueryTimeSeries200Response`** |  | [QueryTimeSeries200Response](QueryTimeSeries200Response.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

