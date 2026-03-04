# TimeseriesJsonResult


**Source:** `waylay.services.data.models.timeseries_json_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**SeriesQueryResponse**](SeriesQueryResponse.md) |  | 
**series** | **List[List[SeriesValue]]** | Array of timestamp-value tuples | 


## Example

```python
from waylay.services.data.models.timeseries_json_result import TimeseriesJsonResult

timeseries_json_result = TimeseriesJsonResult(query=..., series=...)

# Create from JSON
timeseries_json_result = TimeseriesJsonResult.from_json(
    '{ "query": ..., "series": ... }'
)

# Export to dictionary
timeseries_json_result_dict = timeseries_json_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


