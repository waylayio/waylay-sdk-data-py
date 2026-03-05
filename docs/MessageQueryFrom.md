# MessageQueryFrom

The lower bound of the time range to retrieve message from

**Source:** `waylay.services.data.models.message_query_from`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
**int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds.
**datetime** | -

## Example

```python
from waylay.services.data.models.message_query_from import MessageQueryFrom

# Use any of the accepted types (see table above)
my_message_query_from: MessageQueryFrom = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


