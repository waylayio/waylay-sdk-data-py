# TimeseriesJsonResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**SeriesQueryResponse**](SeriesQueryResponse.md) |  | 
**series** | **List[List[SeriesKeyValueInner]]** | Array of timestamp-value tuples | 

## Example

```python
from waylay.services.data.models.timeseries_json_result import TimeseriesJsonResult

# TODO update the JSON string below
json = "{}"
# create an instance of TimeseriesJsonResult from a JSON string
timeseries_json_result_instance = TimeseriesJsonResult.from_json(json)
# print the JSON string representation of the object
print TimeseriesJsonResult.to_json()

# convert the object into a dict
timeseries_json_result_dict = timeseries_json_result_instance.to_dict()
# create an instance of TimeseriesJsonResult from a dict
timeseries_json_result_form_dict = timeseries_json_result.from_dict(timeseries_json_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


