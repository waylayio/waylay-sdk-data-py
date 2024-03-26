# SeriesQueryResponse


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

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesQueryResponse from a JSON string
series_query_response_instance = SeriesQueryResponse.from_json(json)
# print the JSON string representation of the object
print SeriesQueryResponse.to_json()

# convert the object into a dict
series_query_response_dict = series_query_response_instance.to_dict()
# create an instance of SeriesQueryResponse from a dict
series_query_response_form_dict = series_query_response.from_dict(series_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


