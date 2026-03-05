# MessageQueryResultItem


**Source:** `waylay.services.data.models.message_query_result_item`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Primary identifier of a _Resource_ | [optional] 
**messages** | [**List[TimestampedEvent]**](TimestampedEvent.md) |  | [optional] 


## Example

```python
from waylay.services.data.models.message_query_result_item import MessageQueryResultItem

message_query_result_item = MessageQueryResultItem(resource=..., messages=...)

# Create from JSON
message_query_result_item = MessageQueryResultItem.from_json(
    '{ "resource": ..., "messages": ... }'
)

# Export to dictionary
message_query_result_item_dict = message_query_result_item.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


