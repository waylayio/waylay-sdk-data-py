# MessageQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | **List[str]** | The list of resources to retrieve the messages for | 
**limit** | **int** | The number of messages per resource to retrieve | 
**var_from** | [**MessageQueryFrom**](MessageQueryFrom.md) |  | [optional] 
**until** | [**MessageQueryUntil**](MessageQueryUntil.md) |  | [optional] 
**window** | [**MessageQueryWindow**](MessageQueryWindow.md) |  | [optional] 

## Example

```python
from waylay.services.data.models.message_query import MessageQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MessageQuery from a JSON string
message_query_instance = MessageQuery.from_json(json)
# print the JSON string representation of the object
print MessageQuery.to_json()

# convert the object into a dict
message_query_dict = message_query_instance.to_dict()
# create an instance of MessageQuery from a dict
message_query_form_dict = message_query.from_dict(message_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


