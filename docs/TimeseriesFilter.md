# TimeseriesFilter

Filter that will be applied to datapoints *before* aggregation is performed.

**Source:** `waylay.services.data.models.timeseries_filter`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**TimeseriesFilterOperatorOperator**](TimeseriesFilterOperatorOperator.md) |  | 
**value** | [**TimeseriesFilterValueExactValue**](TimeseriesFilterValueExactValue.md) |  | 
**lower_bound** | **float** |  | 
**upper_bound** | **float** |  | 


## Example

```python
from waylay.services.data.models.timeseries_filter import TimeseriesFilter

timeseries_filter = TimeseriesFilter(
    operator=..., value=..., lower_bound=..., upper_bound=...
)

# Create from JSON
timeseries_filter = TimeseriesFilter.from_json(
    '{ "operator": ..., "value": ..., "lowerBound": ..., "upperBound": ... }'
)

# Export to dictionary
timeseries_filter_dict = timeseries_filter.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


