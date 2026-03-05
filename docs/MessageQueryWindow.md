# MessageQueryWindow

A duration expression. Will be evaluated vs `from`, `until` or the query execution date to get the actual time range

**Source:** `waylay.services.data.models.message_query_window`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
**str** | Time interval with duration unit.
**datetime** | -

## Example

```python
from waylay.services.data.models.message_query_window import MessageQueryWindow

# Use any of the accepted types (see table above)
my_message_query_window: MessageQueryWindow = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


