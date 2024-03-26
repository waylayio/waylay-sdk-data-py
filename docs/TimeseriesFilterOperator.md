# TimeseriesFilterOperator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | [**TimeseriesFilterOperatorOperator**](TimeseriesFilterOperatorOperator.md) |  | 

## Example

```python
from waylay.services.data.models.timeseries_filter_operator import TimeseriesFilterOperator

# TODO update the JSON string below
json = "{}"
# create an instance of TimeseriesFilterOperator from a JSON string
timeseries_filter_operator_instance = TimeseriesFilterOperator.from_json(json)
# print the JSON string representation of the object
print TimeseriesFilterOperator.to_json()

# convert the object into a dict
timeseries_filter_operator_dict = timeseries_filter_operator_instance.to_dict()
# create an instance of TimeseriesFilterOperator from a dict
timeseries_filter_operator_form_dict = timeseries_filter_operator.from_dict(timeseries_filter_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


