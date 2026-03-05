# PostSeriesForResourceRequest


**Source:** `waylay.services.data.models.post_series_for_resource_request`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
[**Event**](Event.md) | -
[**List[Event]**](Event.md) | Array of measurement objects with optional event timestamp.

## Example

```python
from waylay.services.data.models.post_series_for_resource_request import (
    PostSeriesForResourceRequest,
)

# Use any of the accepted types (see table above)
my_post_series_for_resource_request: PostSeriesForResourceRequest = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


