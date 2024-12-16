# SeriesQueryWithoutAggregatesRequest


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

## Example

```python
from waylay.services.data.models.series_query_without_aggregates_request import SeriesQueryWithoutAggregatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesQueryWithoutAggregatesRequest from a JSON string
series_query_without_aggregates_request_instance = SeriesQueryWithoutAggregatesRequest.from_json(json)
# print the JSON string representation of the object
print SeriesQueryWithoutAggregatesRequest.to_json()

# convert the object into a dict
series_query_without_aggregates_request_dict = series_query_without_aggregates_request_instance.to_dict()
# create an instance of SeriesQueryWithoutAggregatesRequest from a dict
series_query_without_aggregates_request_form_dict = series_query_without_aggregates_request.from_dict(series_query_without_aggregates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


