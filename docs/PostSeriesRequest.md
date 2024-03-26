# PostSeriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Primary identifier of a _Resource_ | 
**timestamp** | [**EventTimestamp**](EventTimestamp.md) |  | [optional] 

## Example

```python
from waylay.services.data.models.post_series_request import PostSeriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSeriesRequest from a JSON string
post_series_request_instance = PostSeriesRequest.from_json(json)
# print the JSON string representation of the object
print PostSeriesRequest.to_json()

# convert the object into a dict
post_series_request_dict = post_series_request_instance.to_dict()
# create an instance of PostSeriesRequest from a dict
post_series_request_form_dict = post_series_request.from_dict(post_series_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


