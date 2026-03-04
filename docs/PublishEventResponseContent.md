# PublishEventResponseContent


**Source:** `waylay.services.data.models.publish_event_response_content`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
[**TimestampedResourceEvent**](TimestampedResourceEvent.md) | -
[**List[TimestampedResourceEvent]**](TimestampedResourceEvent.md) | Array of measurement objects with resource identifier and timestamp.
[**PublishEventResponseObjectObject**](PublishEventResponseObjectObject.md) | -

## Example

```python
from waylay.services.data.models.publish_event_response_content import (
    PublishEventResponseContent,
)

# Use any of the accepted types (see table above)
my_publish_event_response_content: PublishEventResponseContent = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


