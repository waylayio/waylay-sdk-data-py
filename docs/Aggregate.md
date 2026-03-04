# Aggregate


**Source:** `waylay.services.data.models.aggregate`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**MIN** | `'min'` |
**MAX** | `'max'` |
**MEAN** | `'mean'` |
**MEDIAN** | `'median'` |
**SUM** | `'sum'` |
**COUNT** | `'count'` |
**COUNT_MINUS_NON_MINUS_NUMERIC** | `'count-non-numeric'` |
**COUNT_MINUS_NUMERIC** | `'count-numeric'` |
**FIRST** | `'first'` |
**LAST** | `'last'` |
**STD** | `'std'` |
**DIFF** | `'diff'` |

## Example

```python
from waylay.services.data.models.aggregate import Aggregate

# Use enum by value
my_aggregate = Aggregate.MIN
print(my_aggregate)  # Output: 'min'

# Or by string value
my_aggregate = Aggregate("min")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


