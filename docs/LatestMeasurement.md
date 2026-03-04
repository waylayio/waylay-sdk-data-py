# LatestMeasurement

The latest measurement of a series.

**Source:** `waylay.services.data.models.latest_measurement`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds. | [optional] 


## Example

```python
from waylay.services.data.models.latest_measurement import LatestMeasurement

latest_measurement = LatestMeasurement(timestamp=...)

# Create from JSON
latest_measurement = LatestMeasurement.from_json('{ "timestamp": ... }')

# Export to dictionary
latest_measurement_dict = latest_measurement.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


