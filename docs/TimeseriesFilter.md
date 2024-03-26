# TimeseriesFilter

Filter that will be applied to datapoints *before* aggregation is performed.

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

# TODO update the JSON string below
json = "{}"
# create an instance of TimeseriesFilter from a JSON string
timeseries_filter_instance = TimeseriesFilter.from_json(json)
# print the JSON string representation of the object
print TimeseriesFilter.to_json()

# convert the object into a dict
timeseries_filter_dict = timeseries_filter_instance.to_dict()
# create an instance of TimeseriesFilter from a dict
timeseries_filter_form_dict = timeseries_filter.from_dict(timeseries_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


