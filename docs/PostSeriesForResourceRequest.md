# PostSeriesForResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | [**EventTimestamp**](EventTimestamp.md) |  | [optional] 

## Example

```python
from waylay.services.data.models.post_series_for_resource_request import PostSeriesForResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSeriesForResourceRequest from a JSON string
post_series_for_resource_request_instance = PostSeriesForResourceRequest.from_json(json)
# print the JSON string representation of the object
print PostSeriesForResourceRequest.to_json()

# convert the object into a dict
post_series_for_resource_request_dict = post_series_for_resource_request_instance.to_dict()
# create an instance of PostSeriesForResourceRequest from a dict
post_series_for_resource_request_form_dict = post_series_for_resource_request.from_dict(post_series_for_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


