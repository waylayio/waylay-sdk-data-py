# TimestampedEvent

Measurement object with timestamp

**Source:** `waylay.services.data.models.timestamped_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Event timestamp | 


## Example

```python
from waylay.services.data.models.timestamped_event import TimestampedEvent

timestamped_event = TimestampedEvent(timestamp=...)

# Create from JSON
timestamped_event = TimestampedEvent.from_json('{ "timestamp": ... }')

# Export to dictionary
timestamped_event_dict = timestamped_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


