# ObjectData

Event data stored only in the _Message Cache_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.data.models.object_data import ObjectData

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectData from a JSON string
object_data_instance = ObjectData.from_json(json)
# print the JSON string representation of the object
print ObjectData.to_json()

# convert the object into a dict
object_data_dict = object_data_instance.to_dict()
# create an instance of ObjectData from a dict
object_data_form_dict = object_data.from_dict(object_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


