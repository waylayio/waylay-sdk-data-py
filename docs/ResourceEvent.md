# ResourceEvent

Measurement object with resource identifier and optional timestamp.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Primary identifier of a _Resource_ | 
**timestamp** | [**EventTimestamp**](EventTimestamp.md) |  | [optional] 

## Example

```python
from waylay.services.data.models.resource_event import ResourceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceEvent from a JSON string
resource_event_instance = ResourceEvent.from_json(json)
# print the JSON string representation of the object
print ResourceEvent.to_json()

# convert the object into a dict
resource_event_dict = resource_event_instance.to_dict()
# create an instance of ResourceEvent from a dict
resource_event_form_dict = resource_event.from_dict(resource_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


