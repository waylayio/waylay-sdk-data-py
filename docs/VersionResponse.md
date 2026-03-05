# VersionResponse


**Source:** `waylay.services.data.models.version_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**name** | **str** |  | 
**message** | **str** |  | [optional] 


## Example

```python
from waylay.services.data.models.version_response import VersionResponse

version_response = VersionResponse(version=..., name=..., message=...)

# Create from JSON
version_response = VersionResponse.from_json(
    '{ "version": ..., "name": ..., "message": ... }'
)

# Export to dictionary
version_response_dict = version_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


