# Grouping


**Source:** `waylay.services.data.models.grouping`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
[**GroupingAuto**](GroupingAuto.md) | -
**str** | Time interval with duration unit.
**str** | A [ISO8601 Duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) with day (`D`), hour (`H`), minute (`M`) and second (`S`) specifiers.

## Example

```python
from waylay.services.data.models.grouping import Grouping

# Use any of the accepted types (see table above)
my_grouping: Grouping = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


