# MessageQuery


**Source:** `waylay.services.data.models.message_query`




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

message_query = MessageQuery(
    resources=..., limit=..., var_from=..., until=..., window=...
)

# Create from JSON
message_query = MessageQuery.from_json(
    '{ "resources": ..., "limit": ..., "from": ..., "until": ..., "window": ... }'
)

# Export to dictionary
message_query_dict = message_query.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


