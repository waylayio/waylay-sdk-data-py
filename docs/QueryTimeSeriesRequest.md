# QueryTimeSeriesRequest


**Source:** `waylay.services.data.models.query_time_series_request`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
[**SeriesQueryRequest**](SeriesQueryRequest.md) | -
[**SeriesQueryWithoutAggregatesRequest**](SeriesQueryWithoutAggregatesRequest.md) | -
[**List[SeriesQueryItem]**](SeriesQueryItem.md) | -

## Example

```python
from waylay.services.data.models.query_time_series_request import QueryTimeSeriesRequest

# Use any of the accepted types (see table above)
my_query_time_series_request: QueryTimeSeriesRequest = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


