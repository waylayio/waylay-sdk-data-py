# Event

Measurement object with optional event timestamp.

**Source:** `waylay.services.data.models.event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | [**EventTimestamp**](EventTimestamp.md) |  | [optional] 


## Example

```python
from waylay.services.data.models.event import Event

event = Event(timestamp=...)

# Create from JSON
event = Event.from_json('{ "timestamp": ... }')

# Export to dictionary
event_dict = event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


