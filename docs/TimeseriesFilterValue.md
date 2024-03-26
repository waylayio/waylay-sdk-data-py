# TimeseriesFilterValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**TimeseriesFilterValueExactValue**](TimeseriesFilterValueExactValue.md) |  | 
**lower_bound** | **float** |  | 
**upper_bound** | **float** |  | 

## Example

```python
from waylay.services.data.models.timeseries_filter_value import TimeseriesFilterValue

# TODO update the JSON string below
json = "{}"
# create an instance of TimeseriesFilterValue from a JSON string
timeseries_filter_value_instance = TimeseriesFilterValue.from_json(json)
# print the JSON string representation of the object
print TimeseriesFilterValue.to_json()

# convert the object into a dict
timeseries_filter_value_dict = timeseries_filter_value_instance.to_dict()
# create an instance of TimeseriesFilterValue from a dict
timeseries_filter_value_form_dict = timeseries_filter_value.from_dict(timeseries_filter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


