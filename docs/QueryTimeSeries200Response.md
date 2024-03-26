# QueryTimeSeries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**SeriesQueryResponse**](SeriesQueryResponse.md) |  | 
**series** | **List[List[SeriesKeyValueInner]]** | Array of timestamp-value tuples | 

## Example

```python
from waylay.services.data.models.query_time_series200_response import QueryTimeSeries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTimeSeries200Response from a JSON string
query_time_series200_response_instance = QueryTimeSeries200Response.from_json(json)
# print the JSON string representation of the object
print QueryTimeSeries200Response.to_json()

# convert the object into a dict
query_time_series200_response_dict = query_time_series200_response_instance.to_dict()
# create an instance of QueryTimeSeries200Response from a dict
query_time_series200_response_form_dict = query_time_series200_response.from_dict(query_time_series200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


