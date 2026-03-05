# PostSeriesRequest


**Source:** `waylay.services.data.models.post_series_request`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
[**ResourceEvent**](ResourceEvent.md) | -
[**List[ResourceEvent]**](ResourceEvent.md) | Array of measurement objects with resource identifier and optional timestamp.

## Example

```python
from waylay.services.data.models.post_series_request import PostSeriesRequest

# Use any of the accepted types (see table above)
my_post_series_request: PostSeriesRequest = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


