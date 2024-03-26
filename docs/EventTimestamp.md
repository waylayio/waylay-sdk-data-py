# EventTimestamp

Event timestamp, if not specified, the _processing timestamp_ of the broker will added as `timestamp` attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.data.models.event_timestamp import EventTimestamp

# TODO update the JSON string below
json = "{}"
# create an instance of EventTimestamp from a JSON string
event_timestamp_instance = EventTimestamp.from_json(json)
# print the JSON string representation of the object
print EventTimestamp.to_json()

# convert the object into a dict
event_timestamp_dict = event_timestamp_instance.to_dict()
# create an instance of EventTimestamp from a dict
event_timestamp_form_dict = event_timestamp.from_dict(event_timestamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


