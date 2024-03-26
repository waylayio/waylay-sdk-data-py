# TTLDuration

Specifies the duration of a TTL interval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.data.models.ttl_duration import TTLDuration

# TODO update the JSON string below
json = "{}"
# create an instance of TTLDuration from a JSON string
ttl_duration_instance = TTLDuration.from_json(json)
# print the JSON string representation of the object
print TTLDuration.to_json()

# convert the object into a dict
ttl_duration_dict = ttl_duration_instance.to_dict()
# create an instance of TTLDuration from a dict
ttl_duration_form_dict = ttl_duration.from_dict(ttl_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


