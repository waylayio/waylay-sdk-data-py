# ResourceEvent

Measurement object with resource identifier and optional timestamp.

**Source:** `waylay.services.data.models.resource_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Primary identifier of a _Resource_ | 
**timestamp** | [**EventTimestamp**](EventTimestamp.md) |  | [optional] 


## Example

```python
from waylay.services.data.models.resource_event import ResourceEvent

resource_event = ResourceEvent(resource=..., timestamp=...)

# Create from JSON
resource_event = ResourceEvent.from_json('{ "resource": ..., "timestamp": ... }')

# Export to dictionary
resource_event_dict = resource_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


