# TimeseriesFilterValueBounds


**Source:** `waylay.services.data.models.timeseries_filter_value_bounds`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lower_bound** | **float** |  | 
**upper_bound** | **float** |  | 


## Example

```python
from waylay.services.data.models.timeseries_filter_value_bounds import (
    TimeseriesFilterValueBounds,
)

timeseries_filter_value_bounds = TimeseriesFilterValueBounds(
    lower_bound=..., upper_bound=...
)

# Create from JSON
timeseries_filter_value_bounds = TimeseriesFilterValueBounds.from_json(
    '{ "lowerBound": ..., "upperBound": ... }'
)

# Export to dictionary
timeseries_filter_value_bounds_dict = timeseries_filter_value_bounds.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


