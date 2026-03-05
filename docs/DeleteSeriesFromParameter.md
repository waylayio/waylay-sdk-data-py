# DeleteSeriesFromParameter


**Source:** `waylay.services.data.models.delete_series_from_parameter`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
**int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds.
**str** | Time interval with duration unit.

## Example

```python
from waylay.services.data.models.delete_series_from_parameter import (
    DeleteSeriesFromParameter,
)

# Use any of the accepted types (see table above)
my_delete_series_from_parameter: DeleteSeriesFromParameter = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


