# GetDatapointsForMetricRaw200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**GetDatapointsForMetricRaw200ResponseLinks**](GetDatapointsForMetricRaw200ResponseLinks.md) |  | [optional] 
**query** | [**SeriesQueryResponse**](SeriesQueryResponse.md) |  | 
**series** | **List[List[SeriesKeyValueInner]]** | Array of timestamp-value tuples | 

## Example

```python
from waylay.services.data.models.get_datapoints_for_metric_raw200_response import GetDatapointsForMetricRaw200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatapointsForMetricRaw200Response from a JSON string
get_datapoints_for_metric_raw200_response_instance = GetDatapointsForMetricRaw200Response.from_json(json)
# print the JSON string representation of the object
print GetDatapointsForMetricRaw200Response.to_json()

# convert the object into a dict
get_datapoints_for_metric_raw200_response_dict = get_datapoints_for_metric_raw200_response_instance.to_dict()
# create an instance of GetDatapointsForMetricRaw200Response from a dict
get_datapoints_for_metric_raw200_response_form_dict = get_datapoints_for_metric_raw200_response.from_dict(get_datapoints_for_metric_raw200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


