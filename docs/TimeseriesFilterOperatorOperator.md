# TimeseriesFilterOperatorOperator


**Source:** `waylay.services.data.models.timeseries_filter_operator_operator`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**GT** | `'gt'` |
**GTE** | `'gte'` |
**LT** | `'lt'` |
**LTE** | `'lte'` |
**EQ** | `'eq'` |
**NE** | `'ne'` |
**BETWEEN** | `'between'` |

## Example

```python
from waylay.services.data.models.timeseries_filter_operator_operator import (
    TimeseriesFilterOperatorOperator,
)

# Use enum by value
my_timeseries_filter_operator_operator = TimeseriesFilterOperatorOperator.GT
print(my_timeseries_filter_operator_operator)  # Output: 'gt'

# Or by string value
my_timeseries_filter_operator_operator = TimeseriesFilterOperatorOperator("gt")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


