# waylay.services.data.VersionApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health**](VersionApi.md#health) | **GET** /data/v1/ | Version

# **health**
> health(
> headers
> ) -> VersionResponse

Version

Gets the status and version of the service.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Model classes for responses/parameters are available only when `waylay-sdk-data-types` is installed
from waylay.services.data.models.version_response import VersionResponse
try:
    # Version
    # calls `GET /data/v1/`
    api_response = await waylay_client.data.version.health(
    )
    print("The response of data.version.health:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling data.version.health: %s\n" % e)
```

### Endpoint
```
GET /data/v1/
```
### Parameters

This endpoint does not need any parameter.
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`VersionResponse`** |  | [VersionResponse](VersionResponse.md)
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

