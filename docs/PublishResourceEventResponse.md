# PublishResourceEventResponse


**Source:** `waylay.services.data.models.publish_resource_event_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**content** | [**PublishResourceEventResponseContent**](PublishResourceEventResponseContent.md) |  | [optional] 


## Example

```python
from waylay.services.data.models.publish_resource_event_response import (
    PublishResourceEventResponse,
)

publish_resource_event_response = PublishResourceEventResponse(message=..., content=...)

# Create from JSON
publish_resource_event_response = PublishResourceEventResponse.from_json(
    '{ "message": ..., "content": ... }'
)

# Export to dictionary
publish_resource_event_response_dict = publish_resource_event_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


