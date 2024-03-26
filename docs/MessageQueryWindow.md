# MessageQueryWindow

A duration expression. Will be evaluated vs `from`, `until` or the query execution date to get the actual time range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.data.models.message_query_window import MessageQueryWindow

# TODO update the JSON string below
json = "{}"
# create an instance of MessageQueryWindow from a JSON string
message_query_window_instance = MessageQueryWindow.from_json(json)
# print the JSON string representation of the object
print MessageQueryWindow.to_json()

# convert the object into a dict
message_query_window_dict = message_query_window_instance.to_dict()
# create an instance of MessageQueryWindow from a dict
message_query_window_form_dict = message_query_window.from_dict(message_query_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


