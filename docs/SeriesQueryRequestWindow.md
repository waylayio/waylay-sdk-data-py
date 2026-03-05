# SeriesQueryRequestWindow


**Source:** `waylay.services.data.models.series_query_request_window`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
**str** | Time interval with duration unit.
**str** | A [ISO8601 Duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) with day (`D`), hour (`H`), minute (`M`) and second (`S`) specifiers.

## Example

```python
from waylay.services.data.models.series_query_request_window import (
    SeriesQueryRequestWindow,
)

# Use any of the accepted types (see table above)
my_series_query_request_window: SeriesQueryRequestWindow = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


