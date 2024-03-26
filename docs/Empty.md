# Empty

Marks that multiple events where published

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.data.models.empty import Empty

# TODO update the JSON string below
json = "{}"
# create an instance of Empty from a JSON string
empty_instance = Empty.from_json(json)
# print the JSON string representation of the object
print Empty.to_json()

# convert the object into a dict
empty_dict = empty_instance.to_dict()
# create an instance of Empty from a dict
empty_form_dict = empty.from_dict(empty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


