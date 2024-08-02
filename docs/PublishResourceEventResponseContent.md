# PublishResourceEventResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Event timestamp | 

## Example

```python
from waylay.services.data.models.publish_resource_event_response_content import PublishResourceEventResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of PublishResourceEventResponseContent from a JSON string
publish_resource_event_response_content_instance = PublishResourceEventResponseContent.from_json(json)
# print the JSON string representation of the object
print PublishResourceEventResponseContent.to_json()

# convert the object into a dict
publish_resource_event_response_content_dict = publish_resource_event_response_content_instance.to_dict()
# create an instance of PublishResourceEventResponseContent from a dict
publish_resource_event_response_content_form_dict = publish_resource_event_response_content.from_dict(publish_resource_event_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


