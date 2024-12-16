# MultipleSeriesQueryRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**SeriesQueryRequestFrom**](SeriesQueryRequestFrom.md) |  | [optional] 
**until** | [**SeriesQueryRequestFrom**](SeriesQueryRequestFrom.md) |  | [optional] 
**window** | [**SeriesQueryRequestWindow**](SeriesQueryRequestWindow.md) |  | [optional] 
**metric** | **str** | Key that identifies a single timeseries for a given _Resource_. Corresponds with the top-level keys of _Message Events_  that are processed by the broker for that _Resource_. | 
**aggregates** | **List[object]** |  | 
**grouping** | [**Grouping**](Grouping.md) |  | [optional] 
**resources** | **List[str]** |  | 
**max_results** | **int** |  | [optional] 
**filter** | [**TimeseriesFilter**](TimeseriesFilter.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] [default to Order.ASCENDING]

## Example

```python
from waylay.services.data.models.multiple_series_query_request_inner import MultipleSeriesQueryRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleSeriesQueryRequestInner from a JSON string
multiple_series_query_request_inner_instance = MultipleSeriesQueryRequestInner.from_json(json)
# print the JSON string representation of the object
print MultipleSeriesQueryRequestInner.to_json()

# convert the object into a dict
multiple_series_query_request_inner_dict = multiple_series_query_request_inner_instance.to_dict()
# create an instance of MultipleSeriesQueryRequestInner from a dict
multiple_series_query_request_inner_form_dict = multiple_series_query_request_inner.from_dict(multiple_series_query_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


