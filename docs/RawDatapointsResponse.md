# RawDatapointsResponse


**Source:** `waylay.services.data.models.raw_datapoints_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**RawDatapointsLinks**](RawDatapointsLinks.md) |  | [optional] 
**query** | [**SeriesQueryResponse**](SeriesQueryResponse.md) |  | 
**series** | **List[List[SeriesValue]]** | Array of timestamp-value tuples | 


## Example

```python
from waylay.services.data.models.raw_datapoints_response import RawDatapointsResponse

raw_datapoints_response = RawDatapointsResponse(links=..., query=..., series=...)

# Create from JSON
raw_datapoints_response = RawDatapointsResponse.from_json(
    '{ "_links": ..., "query": ..., "series": ... }'
)

# Export to dictionary
raw_datapoints_response_dict = raw_datapoints_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


