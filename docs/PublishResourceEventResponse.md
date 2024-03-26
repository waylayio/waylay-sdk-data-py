# PublishResourceEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**content** | [**PublishResourceEventResponseContent**](PublishResourceEventResponseContent.md) |  | [optional] 

## Example

```python
from waylay.services.data.models.publish_resource_event_response import PublishResourceEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublishResourceEventResponse from a JSON string
publish_resource_event_response_instance = PublishResourceEventResponse.from_json(json)
# print the JSON string representation of the object
print PublishResourceEventResponse.to_json()

# convert the object into a dict
publish_resource_event_response_dict = publish_resource_event_response_instance.to_dict()
# create an instance of PublishResourceEventResponse from a dict
publish_resource_event_response_form_dict = publish_resource_event_response.from_dict(publish_resource_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


