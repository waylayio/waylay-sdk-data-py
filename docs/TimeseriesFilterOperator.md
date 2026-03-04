# TimeseriesFilterOperator


**Source:** `waylay.services.data.models.timeseries_filter_operator`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**TimeseriesFilterOperatorOperator**](TimeseriesFilterOperatorOperator.md) |  | 


## Example

```python
from waylay.services.data.models.timeseries_filter_operator import (
    TimeseriesFilterOperator,
)

timeseries_filter_operator = TimeseriesFilterOperator(operator=...)

# Create from JSON
timeseries_filter_operator = TimeseriesFilterOperator.from_json('{ "operator": ... }')

# Export to dictionary
timeseries_filter_operator_dict = timeseries_filter_operator.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


