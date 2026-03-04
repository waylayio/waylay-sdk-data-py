# PublishEventResponse


**Source:** `waylay.services.data.models.publish_event_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**content** | [**PublishEventResponseContent**](PublishEventResponseContent.md) |  | [optional] 


## Example

```python
from waylay.services.data.models.publish_event_response import PublishEventResponse

publish_event_response = PublishEventResponse(message=..., content=...)

# Create from JSON
publish_event_response = PublishEventResponse.from_json(
    '{ "message": ..., "content": ... }'
)

# Export to dictionary
publish_event_response_dict = publish_event_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


