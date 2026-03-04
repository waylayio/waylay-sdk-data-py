# MetricSummary


**Source:** `waylay.services.data.models.metric_summary`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Key that identifies a single timeseries for a given _Resource_. Corresponds with the top-level keys of _Message Events_  that are processed by the broker for that _Resource_. | 
**latest** | [**LatestValue**](LatestValue.md) |  | [optional] 


## Example

```python
from waylay.services.data.models.metric_summary import MetricSummary

metric_summary = MetricSummary(name=..., latest=...)

# Create from JSON
metric_summary = MetricSummary.from_json('{ "name": ..., "latest": ... }')

# Export to dictionary
metric_summary_dict = metric_summary.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


