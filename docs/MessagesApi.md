# waylay.services.data.MessagesApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_messages**](MessagesApi.md#delete_messages) | **DELETE** /data/v1/messages/{resourceId} | Remove Messages For Resource
[**get_latest_document**](MessagesApi.md#get_latest_document) | **GET** /data/v1/messages/{resourceId}/current | Retrieve Latest Message
[**get_latest_messages**](MessagesApi.md#get_latest_messages) | **GET** /data/v1/messages/{resourceId} | Retrieve Messages For Resource
[**query_messages**](MessagesApi.md#query_messages) | **POST** /data/v1/messages/query | Query Messages

# **delete_messages**
> delete_messages(
> resource_id: str,
> headers
> ) -> DeleteMessages200Response

Remove Messages For Resource

Removes all messages associated with a resource.

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
    # Remove Messages For Resource
    # calls `DELETE /data/v1/messages/{resourceId}`
    api_response = await waylay_client.data.messages.delete_messages(
        'resource_id_example', # resource_id | path param "resourceId"
    )
    print("The response of data.messages.delete_messages:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.messages.delete_messages: %s\n" % e)
```

### Endpoint
```
DELETE /data/v1/messages/{resourceId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **str** | path parameter `"resourceId"` | Uniquely identifies a resource. | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_document**
> get_latest_document(
> resource_id: str,
> headers
> ) -> TimestampedEvent

Retrieve Latest Message

Retrieves the latest (i.e. most recent) message for a resource.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.data.models.timestamped_event import TimestampedEvent
try:
    # Retrieve Latest Message
    # calls `GET /data/v1/messages/{resourceId}/current`
    api_response = await waylay_client.data.messages.get_latest_document(
        'resource_id_example', # resource_id | path param "resourceId"
    )
    print("The response of data.messages.get_latest_document:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.messages.get_latest_document: %s\n" % e)
```

### Endpoint
```
GET /data/v1/messages/{resourceId}/current
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **str** | path parameter `"resourceId"` | Uniquely identifies a resource. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TimestampedEvent`** |  | [TimestampedEvent](TimestampedEvent.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | No Message Received Yet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_messages**
> get_latest_messages(
> resource_id: str,
> headers
> ) -> List[TimestampedEvent]

Retrieve Messages For Resource

Retrieves the last n messages for a resource.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.data.models.timestamped_event import TimestampedEvent
try:
    # Retrieve Messages For Resource
    # calls `GET /data/v1/messages/{resourceId}`
    api_response = await waylay_client.data.messages.get_latest_messages(
        'resource_id_example', # resource_id | path param "resourceId"
    )
    print("The response of data.messages.get_latest_messages:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.messages.get_latest_messages: %s\n" % e)
```

### Endpoint
```
GET /data/v1/messages/{resourceId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **str** | path parameter `"resourceId"` | Uniquely identifies a resource. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`List[TimestampedEvent]`** |  | [List[TimestampedEvent]](TimestampedEvent.md)
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

# **query_messages**
> query_messages(
> headers
> ) -> MessageQueryResult

Query Messages

Executes an ad-hoc messages query.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.data.models.message_query import MessageQuery
from waylay.services.data.models.message_query_result import MessageQueryResult
try:
    # Query Messages
    # calls `POST /data/v1/messages/query`
    api_response = await waylay_client.data.messages.query_messages(
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.data.MessageQuery() # MessageQuery |  (optional)
    )
    print("The response of data.messages.query_messages:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.messages.query_messages: %s\n" % e)
```

### Endpoint
```
POST /data/v1/messages/query
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**MessageQuery**](MessageQuery.md) | json request body |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`MessageQueryResult`** |  | [MessageQueryResult](MessageQueryResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Query Result |  -  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

