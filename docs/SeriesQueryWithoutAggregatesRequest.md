# SeriesQueryWithoutAggregatesRequest


**Source:** `waylay.services.data.models.series_query_without_aggregates_request`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**SeriesQueryRequestFrom**](SeriesQueryRequestFrom.md) |  | [optional] 
**until** | [**SeriesQueryRequestFrom**](SeriesQueryRequestFrom.md) |  | [optional] 
**window** | [**SeriesQueryRequestWindow**](SeriesQueryRequestWindow.md) |  | [optional] 
**metric** | **str** | Key that identifies a single timeseries for a given _Resource_. Corresponds with the top-level keys of _Message Events_  that are processed by the broker for that _Resource_. | 
**aggregates** | **List[object]** |  | [optional] 
**resources** | **List[str]** |  | 
**max_results** | **int** |  | [optional] 
**filter** | [**TimeseriesFilter**](TimeseriesFilter.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] [default to Order.ASCENDING]
**return_ingestion_timestamp** | **bool** |  | [optional] [default to False]


## Example

```python
from waylay.services.data.models.series_query_without_aggregates_request import (
    SeriesQueryWithoutAggregatesRequest,
)

series_query_without_aggregates_request = SeriesQueryWithoutAggregatesRequest(
    var_from=...,
    until=...,
    window=...,
    metric=...,
    aggregates=...,
    resources=...,
    max_results=...,
    filter=...,
    order=...,
    return_ingestion_timestamp=...,
)

# Create from JSON
series_query_without_aggregates_request = SeriesQueryWithoutAggregatesRequest.from_json(
    '{ "from": ..., "until": ..., "window": ..., "metric": ..., "aggregates": ..., "resources": ..., "maxResults": ..., "filter": ..., "order": ..., "returnIngestionTimestamp": ... }'
)

# Export to dictionary
series_query_without_aggregates_request_dict = (
    series_query_without_aggregates_request.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


