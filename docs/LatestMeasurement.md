# LatestMeasurement

The latest measurement of a series.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds. | [optional] 

## Example

```python
from waylay.services.data.models.latest_measurement import LatestMeasurement

# TODO update the JSON string below
json = "{}"
# create an instance of LatestMeasurement from a JSON string
latest_measurement_instance = LatestMeasurement.from_json(json)
# print the JSON string representation of the object
print LatestMeasurement.to_json()

# convert the object into a dict
latest_measurement_dict = latest_measurement_instance.to_dict()
# create an instance of LatestMeasurement from a dict
latest_measurement_form_dict = latest_measurement.from_dict(latest_measurement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


