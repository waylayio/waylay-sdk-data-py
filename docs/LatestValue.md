# LatestValue


**Source:** `waylay.services.data.models.latest_value`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds. | 
**value** | [**ScalarData**](ScalarData.md) |  | [optional] 


## Example

```python
from waylay.services.data.models.latest_value import LatestValue

latest_value = LatestValue(timestamp=..., value=...)

# Create from JSON
latest_value = LatestValue.from_json('{ "timestamp": ..., "value": ... }')

# Export to dictionary
latest_value_dict = latest_value.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


