# MessageQueryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**MessageQuery**](MessageQuery.md) |  | [optional] 
**results** | [**List[MessageQueryResultResultsInner]**](MessageQueryResultResultsInner.md) |  | [optional] 

## Example

```python
from waylay.services.data.models.message_query_result import MessageQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of MessageQueryResult from a JSON string
message_query_result_instance = MessageQueryResult.from_json(json)
# print the JSON string representation of the object
print MessageQueryResult.to_json()

# convert the object into a dict
message_query_result_dict = message_query_result_instance.to_dict()
# create an instance of MessageQueryResult from a dict
message_query_result_form_dict = message_query_result.from_dict(message_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


