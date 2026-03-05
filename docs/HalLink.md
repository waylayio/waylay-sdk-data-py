# HalLink


**Source:** `waylay.services.data.models.hal_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | 
**name** | **str** |  | 


## Example

```python
from waylay.services.data.models.hal_link import HalLink

hal_link = HalLink(href=..., name=...)

# Create from JSON
hal_link = HalLink.from_json('{ "href": ..., "name": ... }')

# Export to dictionary
hal_link_dict = hal_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


