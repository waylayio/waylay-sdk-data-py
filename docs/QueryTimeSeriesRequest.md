# QueryTimeSeriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**SeriesQueryRequestFrom**](SeriesQueryRequestFrom.md) |  | [optional] 
**until** | [**SeriesQueryRequestFrom**](SeriesQueryRequestFrom.md) |  | [optional] 
**window** | [**SeriesQueryRequestWindow**](SeriesQueryRequestWindow.md) |  | [optional] 
**metric** | **str** | Key that identifies a single timeseries for a given _Resource_. Corresponds with the top-level keys of _Message Events_  that are processed by the broker for that _Resource_. | 
**aggregates** | [**List[Aggregate]**](Aggregate.md) |  | 
**grouping** | [**Grouping**](Grouping.md) |  | [optional] 
**resources** | **List[str]** |  | 
**max_results** | **int** |  | [optional] 
**filter** | [**TimeseriesFilter**](TimeseriesFilter.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 

## Example

```python
from waylay.services.data.models.query_time_series_request import QueryTimeSeriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTimeSeriesRequest from a JSON string
query_time_series_request_instance = QueryTimeSeriesRequest.from_json(json)
# print the JSON string representation of the object
print QueryTimeSeriesRequest.to_json()

# convert the object into a dict
query_time_series_request_dict = query_time_series_request_instance.to_dict()
# create an instance of QueryTimeSeriesRequest from a dict
query_time_series_request_form_dict = query_time_series_request.from_dict(query_time_series_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


