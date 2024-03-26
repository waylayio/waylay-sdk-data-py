# GetSeries200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Key that identifies a single timeseries for a given _Resource_. Corresponds with the top-level keys of _Message Events_  that are processed by the broker for that _Resource_. | 
**latest** | [**GetSeries200ResponseInnerLatest**](GetSeries200ResponseInnerLatest.md) |  | [optional] 

## Example

```python
from waylay.services.data.models.get_series200_response_inner import GetSeries200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSeries200ResponseInner from a JSON string
get_series200_response_inner_instance = GetSeries200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetSeries200ResponseInner.to_json()

# convert the object into a dict
get_series200_response_inner_dict = get_series200_response_inner_instance.to_dict()
# create an instance of GetSeries200ResponseInner from a dict
get_series200_response_inner_form_dict = get_series200_response_inner.from_dict(get_series200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


