# ScalarData

Event data stored in both the _Message Cache_ and _Time Series Database_. Keys of these measurements become a _Metric_ for the resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.data.models.scalar_data import ScalarData

# TODO update the JSON string below
json = "{}"
# create an instance of ScalarData from a JSON string
scalar_data_instance = ScalarData.from_json(json)
# print the JSON string representation of the object
print ScalarData.to_json()

# convert the object into a dict
scalar_data_dict = scalar_data_instance.to_dict()
# create an instance of ScalarData from a dict
scalar_data_form_dict = scalar_data.from_dict(scalar_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


