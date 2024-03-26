# MessageQueryResultResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Primary identifier of a _Resource_ | [optional] 
**messages** | [**List[TimestampedEvent]**](TimestampedEvent.md) |  | [optional] 

## Example

```python
from waylay.services.data.models.message_query_result_results_inner import MessageQueryResultResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MessageQueryResultResultsInner from a JSON string
message_query_result_results_inner_instance = MessageQueryResultResultsInner.from_json(json)
# print the JSON string representation of the object
print MessageQueryResultResultsInner.to_json()

# convert the object into a dict
message_query_result_results_inner_dict = message_query_result_results_inner_instance.to_dict()
# create an instance of MessageQueryResultResultsInner from a dict
message_query_result_results_inner_form_dict = message_query_result_results_inner.from_dict(message_query_result_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


