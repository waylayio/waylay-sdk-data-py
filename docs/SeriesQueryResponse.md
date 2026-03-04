# SeriesQueryResponse


**Source:** `waylay.services.data.models.series_query_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds. | [optional] 
**until** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds. | [optional] 
**metric** | **str** | Key that identifies a single timeseries for a given _Resource_. Corresponds with the top-level keys of _Message Events_  that are processed by the broker for that _Resource_. | 
**aggregates** | [**List[Aggregate]**](Aggregate.md) |  | [optional] 
**grouping** | [**Grouping**](Grouping.md) |  | 
**resources** | **List[str]** |  | 
**filter** | [**TimeseriesFilter**](TimeseriesFilter.md) |  | [optional] 
**limit** | **int** |  | [optional] 


## Example

```python
from waylay.services.data.models.series_query_response import SeriesQueryResponse

series_query_response = SeriesQueryResponse(
    var_from=...,
    until=...,
    metric=...,
    aggregates=...,
    grouping=...,
    resources=...,
    filter=...,
    limit=...,
)

# Create from JSON
series_query_response = SeriesQueryResponse.from_json(
    '{ "from": ..., "until": ..., "metric": ..., "aggregates": ..., "grouping": ..., "resources": ..., "filter": ..., "limit": ... }'
)

# Export to dictionary
series_query_response_dict = series_query_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


