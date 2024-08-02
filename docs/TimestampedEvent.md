# TimestampedEvent

Measurement object with timestamp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Event timestamp | 

## Example

```python
from waylay.services.data.models.timestamped_event import TimestampedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimestampedEvent from a JSON string
timestamped_event_instance = TimestampedEvent.from_json(json)
# print the JSON string representation of the object
print TimestampedEvent.to_json()

# convert the object into a dict
timestamped_event_dict = timestamped_event_instance.to_dict()
# create an instance of TimestampedEvent from a dict
timestamped_event_form_dict = timestamped_event.from_dict(timestamped_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


