# TimeseriesFilterValueExact


**Source:** `waylay.services.data.models.timeseries_filter_value_exact`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**TimeseriesFilterValueExactValue**](TimeseriesFilterValueExactValue.md) |  | 


## Example

```python
from waylay.services.data.models.timeseries_filter_value_exact import (
    TimeseriesFilterValueExact,
)

timeseries_filter_value_exact = TimeseriesFilterValueExact(value=...)

# Create from JSON
timeseries_filter_value_exact = TimeseriesFilterValueExact.from_json('{ "value": ... }')

# Export to dictionary
timeseries_filter_value_exact_dict = timeseries_filter_value_exact.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


