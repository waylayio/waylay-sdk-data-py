# MessageQueryResult


**Source:** `waylay.services.data.models.message_query_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**MessageQuery**](MessageQuery.md) |  | [optional] 
**results** | [**List[MessageQueryResultItem]**](MessageQueryResultItem.md) |  | [optional] 


## Example

```python
from waylay.services.data.models.message_query_result import MessageQueryResult

message_query_result = MessageQueryResult(query=..., results=...)

# Create from JSON
message_query_result = MessageQueryResult.from_json('{ "query": ..., "results": ... }')

# Export to dictionary
message_query_result_dict = message_query_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


