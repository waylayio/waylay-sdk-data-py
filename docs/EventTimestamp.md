# EventTimestamp

Event timestamp, if not specified, the _processing timestamp_ of the broker will added as `timestamp` attribute.

**Source:** `waylay.services.data.models.event_timestamp`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
**int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds.
**datetime** | -

## Example

```python
from waylay.services.data.models.event_timestamp import EventTimestamp

# Use any of the accepted types (see table above)
my_event_timestamp: EventTimestamp = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


