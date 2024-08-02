# PublishEventResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Primary identifier of a _Resource_ | 
**timestamp** | **int** | Event timestamp | 

## Example

```python
from waylay.services.data.models.publish_event_response_content import PublishEventResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of PublishEventResponseContent from a JSON string
publish_event_response_content_instance = PublishEventResponseContent.from_json(json)
# print the JSON string representation of the object
print PublishEventResponseContent.to_json()

# convert the object into a dict
publish_event_response_content_dict = publish_event_response_content_instance.to_dict()
# create an instance of PublishEventResponseContent from a dict
publish_event_response_content_form_dict = publish_event_response_content.from_dict(publish_event_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


