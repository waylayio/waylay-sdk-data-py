# GetSeries200ResponseInnerLatest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds. | 
**value** | [**ScalarData**](ScalarData.md) |  | [optional] 

## Example

```python
from waylay.services.data.models.get_series200_response_inner_latest import GetSeries200ResponseInnerLatest

# TODO update the JSON string below
json = "{}"
# create an instance of GetSeries200ResponseInnerLatest from a JSON string
get_series200_response_inner_latest_instance = GetSeries200ResponseInnerLatest.from_json(json)
# print the JSON string representation of the object
print GetSeries200ResponseInnerLatest.to_json()

# convert the object into a dict
get_series200_response_inner_latest_dict = get_series200_response_inner_latest_instance.to_dict()
# create an instance of GetSeries200ResponseInnerLatest from a dict
get_series200_response_inner_latest_form_dict = get_series200_response_inner_latest.from_dict(get_series200_response_inner_latest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


