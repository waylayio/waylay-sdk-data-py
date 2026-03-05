# RawDatapointsLinks


**Source:** `waylay.services.data.models.raw_datapoints_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | [**HalLink**](HalLink.md) |  | [optional] 


## Example

```python
from waylay.services.data.models.raw_datapoints_links import RawDatapointsLinks

raw_datapoints_links = RawDatapointsLinks(next=...)

# Create from JSON
raw_datapoints_links = RawDatapointsLinks.from_json('{ "next": ... }')

# Export to dictionary
raw_datapoints_links_dict = raw_datapoints_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


