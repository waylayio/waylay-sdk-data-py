# TimestampedResourceEvent

Measurement object with resource identifier and timestamp.

**Source:** `waylay.services.data.models.timestamped_resource_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Primary identifier of a _Resource_ | 
**timestamp** | **int** | Event timestamp | 


## Example

```python
from waylay.services.data.models.timestamped_resource_event import (
    TimestampedResourceEvent,
)

timestamped_resource_event = TimestampedResourceEvent(resource=..., timestamp=...)

# Create from JSON
timestamped_resource_event = TimestampedResourceEvent.from_json(
    '{ "resource": ..., "timestamp": ... }'
)

# Export to dictionary
timestamped_resource_event_dict = timestamped_resource_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


