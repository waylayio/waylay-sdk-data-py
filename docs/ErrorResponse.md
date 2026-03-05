# ErrorResponse


**Source:** `waylay.services.data.models.error_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 


## Example

```python
from waylay.services.data.models.error_response import ErrorResponse

error_response = ErrorResponse(error=...)

# Create from JSON
error_response = ErrorResponse.from_json('{ "error": ... }')

# Export to dictionary
error_response_dict = error_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


