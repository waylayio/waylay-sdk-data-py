# HalLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from waylay.services.data.models.hal_link import HalLink

# TODO update the JSON string below
json = "{}"
# create an instance of HalLink from a JSON string
hal_link_instance = HalLink.from_json(json)
# print the JSON string representation of the object
print HalLink.to_json()

# convert the object into a dict
hal_link_dict = hal_link_instance.to_dict()
# create an instance of HalLink from a dict
hal_link_form_dict = hal_link.from_dict(hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


