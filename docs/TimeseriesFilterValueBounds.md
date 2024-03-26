# TimeseriesFilterValueBounds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lower_bound** | **float** |  | 
**upper_bound** | **float** |  | 

## Example

```python
from waylay.services.data.models.timeseries_filter_value_bounds import TimeseriesFilterValueBounds

# TODO update the JSON string below
json = "{}"
# create an instance of TimeseriesFilterValueBounds from a JSON string
timeseries_filter_value_bounds_instance = TimeseriesFilterValueBounds.from_json(json)
# print the JSON string representation of the object
print TimeseriesFilterValueBounds.to_json()

# convert the object into a dict
timeseries_filter_value_bounds_dict = timeseries_filter_value_bounds_instance.to_dict()
# create an instance of TimeseriesFilterValueBounds from a dict
timeseries_filter_value_bounds_form_dict = timeseries_filter_value_bounds.from_dict(timeseries_filter_value_bounds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


