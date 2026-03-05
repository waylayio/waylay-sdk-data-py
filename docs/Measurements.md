# Measurements

Values in an _Event_ payload. Note that only _scalar_ data is stored in the timeseries, while Arrays and objects are only stored in the _Message Cache_.

**Source:** `waylay.services.data.models.measurements`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
[**ScalarData**](ScalarData.md) | -
[**ObjectData**](ObjectData.md) | -

## Example

```python
from waylay.services.data.models.measurements import Measurements

# Use any of the accepted types (see table above)
my_measurements: Measurements = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


