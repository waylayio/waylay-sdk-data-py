# Measurements

Values in an _Event_ payload. Note that only _scalar_ data is stored in the timeseries, while Arrays and objects are only stored in the _Message Cache_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.data.models.measurements import Measurements

# TODO update the JSON string below
json = "{}"
# create an instance of Measurements from a JSON string
measurements_instance = Measurements.from_json(json)
# print the JSON string representation of the object
print Measurements.to_json()

# convert the object into a dict
measurements_dict = measurements_instance.to_dict()
# create an instance of Measurements from a dict
measurements_form_dict = measurements.from_dict(measurements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


