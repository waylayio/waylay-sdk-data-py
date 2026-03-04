# TTLDuration

Specifies the duration of a TTL interval.

**Source:** `waylay.services.data.models.ttl_duration`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
**int** | Number of seconds of a time interval.
**str** | Time interval with duration unit.
**str** | A [ISO8601 Duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) with day (`D`), hour (`H`), minute (`M`) and second (`S`) specifiers.

## Example

```python
from waylay.services.data.models.ttl_duration import TTLDuration

# Use any of the accepted types (see table above)
my_ttl_duration: TTLDuration = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


