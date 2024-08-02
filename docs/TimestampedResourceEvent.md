# TimestampedResourceEvent

Measurement object with resource identifier and timestamp.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Primary identifier of a _Resource_ | 
**timestamp** | **int** | Event timestamp | 

## Example

```python
from waylay.services.data.models.timestamped_resource_event import TimestampedResourceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimestampedResourceEvent from a JSON string
timestamped_resource_event_instance = TimestampedResourceEvent.from_json(json)
# print the JSON string representation of the object
print TimestampedResourceEvent.to_json()

# convert the object into a dict
timestamped_resource_event_dict = timestamped_resource_event_instance.to_dict()
# create an instance of TimestampedResourceEvent from a dict
timestamped_resource_event_form_dict = timestamped_resource_event.from_dict(timestamped_resource_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


