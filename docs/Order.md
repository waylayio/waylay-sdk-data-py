# Order

the order in which the data is returned

**Source:** `waylay.services.data.models.order`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**ASCENDING** | `'ascending'` |
**DESCENDING** | `'descending'` |

## Example

```python
from waylay.services.data.models.order import Order

# Use enum by value
my_order = Order.ASCENDING
print(my_order)  # Output: 'ascending'

# Or by string value
my_order = Order("ascending")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


