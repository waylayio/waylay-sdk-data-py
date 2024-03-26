# waylay.services.data.EventsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_series**](EventsApi.md#post_series) | **POST** /data/v1/events | Post Events
[**post_series_for_resource**](EventsApi.md#post_series_for_resource) | **POST** /data/v1/events/{resourceId} | Post Events For Resource
[**remove**](EventsApi.md#remove) | **DELETE** /data/v1/{resourceId} | Remove Data
[**stream_events**](EventsApi.md#stream_events) | **GET** /data/v1/events/{resourceId} | Stream Events For Resource

# **post_series**
> post_series(
> query: PostSeriesQuery,
> headers
> ) -> PublishEventResponse

Post Events

Pushes events to broker.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.data.models.post_series_request import PostSeriesRequest
from waylay.services.data.models.publish_event_response import PublishEventResponse
try:
    # Post Events
    # calls `POST /data/v1/events`
    api_response = await waylay_client.data.events.post_series(
        # query parameters:
        query = {
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.data.PostSeriesRequest() # PostSeriesRequest |  (optional)
    )
    print("The response of data.events.post_series:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.events.post_series: %s\n" % e)
```

### Endpoint
```
POST /data/v1/events
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**PostSeriesRequest**](PostSeriesRequest.md) | json request body |  | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['forward']** (dict) <br> **query.forward** (Query) | **bool** | query parameter `"forward"` | If payload is a single event, _Events_ are forwarded to the [Rule Engine](/#/api/rules/) unless &#x60;forward&#x60; is explicitly set to &#x60;false&#x60;. If payload has multiple events and each event is for a distinct resource, all _Events_ are forwarded to the [Rule Engine](/#/api/rules/) unless &#x60;forward&#x60; is explicitly set to &#x60;false&#x60; If payload has multiple events and there are multiple events for the same resource, an error will be returned if &#x60;forward&#x60; is explicitly set to &#x60;true&#x60;. | [optional] [default True]
**query['store']** (dict) <br> **query.store** (Query) | **bool** | query parameter `"store"` | Unless explicitly set to &#x60;false&#x60;, _Events_ are stored  into message cache, and their scalar attributes stored in the time series database. | [optional] [default True]
**query['ttl']** (dict) <br> **query.ttl** (Query) | [**TTLDuration**](.md) | query parameter `"ttl"` | Specifies how long data persists in both the message cache and time series database. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PublishEventResponse`** |  | [PublishEventResponse](PublishEventResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event(s) Published |  -  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_series_for_resource**
> post_series_for_resource(
> resource_id: str,
> query: PostSeriesForResourceQuery,
> headers
> ) -> PublishResourceEventResponse

Post Events For Resource

Pushes events for a given resource to broker.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.data.models.post_series_for_resource_request import PostSeriesForResourceRequest
from waylay.services.data.models.publish_resource_event_response import PublishResourceEventResponse
try:
    # Post Events For Resource
    # calls `POST /data/v1/events/{resourceId}`
    api_response = await waylay_client.data.events.post_series_for_resource(
        'resource_id_example', # resource_id | path param "resourceId"
        # query parameters:
        query = {
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.data.PostSeriesForResourceRequest() # PostSeriesForResourceRequest |  (optional)
    )
    print("The response of data.events.post_series_for_resource:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.events.post_series_for_resource: %s\n" % e)
```

### Endpoint
```
POST /data/v1/events/{resourceId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **str** | path parameter `"resourceId"` | Uniquely identifies a resource. | 
**json** | [**PostSeriesForResourceRequest**](PostSeriesForResourceRequest.md) | json request body |  | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['forward']** (dict) <br> **query.forward** (Query) | **bool** | query parameter `"forward"` | If payload is a single event, _Events_ are forwarded to the [Rule Engine](/#/api/rules/) unless &#x60;forward&#x60; is explicitly set to &#x60;false&#x60;. If payload has multiple events, this parameter is ignored and _Events_ will only be stored into message cache and their scalar attributes in the timeseries database. | [optional] [default True]
**query['store']** (dict) <br> **query.store** (Query) | **bool** | query parameter `"store"` | Unless explicitly set to &#x60;false&#x60;, _Events_ are stored  into message cache, and their scalar attributes stored in the time series database. | [optional] [default True]
**query['ttl']** (dict) <br> **query.ttl** (Query) | [**TTLDuration**](.md) | query parameter `"ttl"` | Specifies how long data persists in both the message cache and time series database. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PublishResourceEventResponse`** |  | [PublishResourceEventResponse](PublishResourceEventResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event(s) Published |  -  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove**
> remove(
> resource_id: str,
> query: RemoveQuery,
> headers
> ) -> DeleteMessages200Response

Remove Data

Removes all data for a resource.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.data.models.delete_messages200_response import DeleteMessages200Response
try:
    # Remove Data
    # calls `DELETE /data/v1/{resourceId}`
    api_response = await waylay_client.data.events.remove(
        'resource_id_example', # resource_id | path param "resourceId"
        # query parameters:
        query = {
        },
    )
    print("The response of data.events.remove:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.events.remove: %s\n" % e)
```

### Endpoint
```
DELETE /data/v1/{resourceId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **str** | path parameter `"resourceId"` | Uniquely identifies a resource. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['from']** (dict) <br> **query.var_from** (Query) | [**DeleteSeriesFromParameter**](.md) | query parameter `"from"` | Specifies the lower bound of the time period | [optional] 
**query['until']** (dict) <br> **query.until** (Query) | [**DeleteSeriesFromParameter**](.md) | query parameter `"until"` | Specifies the upper bound of the time period | [optional] 
**query['onlytimeseries']** (dict) <br> **query.onlytimeseries** (Query) | **bool** | query parameter `"onlytimeseries"` | if set to &#x60;true&#x60; will only delete timeseries data | [optional] [default False]
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

# **stream_events**
> stream_events(
> resource_id: str,
> headers
> ) -> TimestampedResourceEvent

Stream Events For Resource

Opens a data stream for the _Events_ of the given _Resource_.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.data.models.timestamped_resource_event import TimestampedResourceEvent
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

### Endpoint
```
GET /data/v1/events/{resourceId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **str** | path parameter `"resourceId"` | Uniquely identifies a resource. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TimestampedResourceEvent`** |  | [TimestampedResourceEvent](TimestampedResourceEvent.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-ndjson, text/event-stream, default

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event Stream |  -  |
**406** | Requested Content Type Not Acceptable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

