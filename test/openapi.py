import json

import yaml


def with_example_provider(dct):
    has_example = False
    if "example" in dct:
        example, has_example = dct["example"], True
    elif "examples" in dct:
        examples = dct["examples"]
        if isinstance(examples, list) and list:
            example, has_example = examples[0], True
    elif "default" in dct:
        example, has_example = dct["default"], True

    if has_example:
        provider = (
            example
            if example is None or isinstance(example, (dict, list, int, float, bool))
            else f"'{example}'"
        )
        dct.update({"$provider": f"lambda: {provider}"})
    return dct


with open("openapi/data.transformed.openapi.yaml", "r") as file:
    OPENAPI_SPEC = yaml.safe_load(file)

MODEL_DEFINITIONS = OPENAPI_SPEC["components"]["schemas"]

_aggregate_model_schema = json.loads(
    r"""{
  "type" : "string",
  "example" : "mean",
  "externalDocs" : {
    "description" : "Possible functions",
    "url" : "https://docs.waylay.io/#/api/broker/?id=aggregates"
  },
  "enum" : [ "min", "max", "mean", "median", "sum", "count", "count-non-numeric", "count-numeric", "first", "last", "std", "diff" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Aggregate": _aggregate_model_schema})

_delete_messages_200_response_model_schema = json.loads(
    r"""{
  "required" : [ "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "deleteMessages_200_response": _delete_messages_200_response_model_schema
})

_delete_series_from_parameter_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/DurationWithUnit"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "deleteSeries_from_parameter": _delete_series_from_parameter_model_schema
})

_error_response_model_schema = json.loads(
    r"""{
  "required" : [ "error" ],
  "type" : "object",
  "properties" : {
    "error" : {
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ErrorResponse": _error_response_model_schema})

_event_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "timestamp" : {
      "$ref" : "#/components/schemas/Event_timestamp"
    }
  },
  "additionalProperties" : {
    "$ref" : "#/components/schemas/Measurements"
  },
  "description" : "Measurement object with optional event timestamp."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Event": _event_model_schema})

_event_timestamp_model_schema = json.loads(
    r"""{
  "title" : "Event_timestamp",
  "description" : "Event timestamp, if not specified, the _processing timestamp_\nof the broker will added as `timestamp` attribute.",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/SO8601Timestamp"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Event_timestamp": _event_timestamp_model_schema})

_get_datapoints_for_metric_raw_200_response_model_schema = json.loads(
    r"""{
  "required" : [ "query", "series" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/getDatapointsForMetricRaw_200_response__links"
    },
    "query" : {
      "$ref" : "#/components/schemas/SeriesQueryResponse"
    },
    "series" : {
      "type" : "array",
      "description" : "Array of timestamp-value tuples",
      "items" : {
        "$ref" : "#/components/schemas/SeriesKeyValue"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "getDatapointsForMetricRaw_200_response": _get_datapoints_for_metric_raw_200_response_model_schema
})

_get_datapoints_for_metric_raw_200_response__links_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "next" : {
      "$ref" : "#/components/schemas/HalLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "getDatapointsForMetricRaw_200_response__links": _get_datapoints_for_metric_raw_200_response__links_model_schema
})

_get_metric_series_from_parameter_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/SO8601Timestamp"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "getMetricSeries_from_parameter": _get_metric_series_from_parameter_model_schema
})

_get_series_200_response_inner_model_schema = json.loads(
    r"""{
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/MetricId"
    },
    "latest" : {
      "$ref" : "#/components/schemas/getSeries_200_response_inner_latest"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "getSeries_200_response_inner": _get_series_200_response_inner_model_schema
})

_get_series_200_response_inner_latest_model_schema = json.loads(
    r"""{
  "required" : [ "timestamp" ],
  "type" : "object",
  "properties" : {
    "timestamp" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    },
    "value" : {
      "$ref" : "#/components/schemas/ScalarData"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "getSeries_200_response_inner_latest": _get_series_200_response_inner_latest_model_schema
})

_grouping_model_schema = json.loads(
    r"""{
  "externalDocs" : {
    "description" : "Possible groupings",
    "url" : "https://docs.waylay.io/#/api/broker/?id=grouping"
  },
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Grouping_anyOf"
  }, {
    "$ref" : "#/components/schemas/DurationWithUnit"
  }, {
    "$ref" : "#/components/schemas/SO8601Duration"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Grouping": _grouping_model_schema})

_grouping_any_of_model_schema = json.loads(
    r"""{
  "title" : "Grouping_anyOf",
  "type" : "string",
  "enum" : [ "auto" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Grouping_anyOf": _grouping_any_of_model_schema})

_hal_link_model_schema = json.loads(
    r"""{
  "required" : [ "href", "name" ],
  "type" : "object",
  "properties" : {
    "href" : {
      "type" : "string",
      "format" : "url",
      "example" : "/series/test1/a/raw?from=1663269720694&until=1665833921682&order=ascending"
    },
    "name" : {
      "type" : "string",
      "example" : "Next series"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HalLink": _hal_link_model_schema})

_latest_measurement_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "timestamp" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    }
  },
  "additionalProperties" : {
    "maxItems" : 1,
    "type" : "array",
    "description" : "The latest value (in a singleton array), keyed by the metric name.",
    "items" : {
      "$ref" : "#/components/schemas/Measurements"
    }
  },
  "description" : "The latest measurement of a series.",
  "example" : {
    "temperature" : [ 13.6 ],
    "timestamp" : 1663269720694
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LatestMeasurement": _latest_measurement_model_schema})

_measurements_model_schema = json.loads(
    r"""{
  "title" : "Measurements",
  "description" : "Values in an _Event_ payload.\nNote that only _scalar_ data is stored in the timeseries, while\nArrays and objects are only stored in the _Message Cache_.",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/ScalarData"
  }, {
    "$ref" : "#/components/schemas/Object_Data"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Measurements": _measurements_model_schema})

_message_query_model_schema = json.loads(
    r"""{
  "required" : [ "limit", "resources" ],
  "type" : "object",
  "properties" : {
    "resources" : {
      "minItems" : 1,
      "type" : "array",
      "description" : "The list of resources to retrieve the messages for",
      "items" : {
        "$ref" : "#/components/schemas/ResourceId"
      }
    },
    "limit" : {
      "minimum" : 1,
      "type" : "integer",
      "description" : "The number of messages per resource to retrieve"
    },
    "from" : {
      "$ref" : "#/components/schemas/MessageQuery_from"
    },
    "until" : {
      "$ref" : "#/components/schemas/MessageQuery_until"
    },
    "window" : {
      "$ref" : "#/components/schemas/MessageQuery_window"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"MessageQuery": _message_query_model_schema})

_message_query_from_model_schema = json.loads(
    r"""{
  "title" : "MessageQuery_from",
  "description" : "The lower bound of the time range to retrieve message from",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/SO8601Timestamp"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"MessageQuery_from": _message_query_from_model_schema})

_message_query_result_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "query" : {
      "$ref" : "#/components/schemas/MessageQuery"
    },
    "results" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/MessageQueryResult_results_inner"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"MessageQueryResult": _message_query_result_model_schema})

_message_query_result_results_inner_model_schema = json.loads(
    r"""{
  "title" : "MessageQueryResult_results_inner",
  "type" : "object",
  "properties" : {
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "messages" : {
      "title" : "messages",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/TimestampedEvent"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "MessageQueryResult_results_inner": _message_query_result_results_inner_model_schema
})

_message_query_until_model_schema = json.loads(
    r"""{
  "title" : "MessageQuery_until",
  "description" : "The upper bound of the time range to retrieve message from",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/SO8601Timestamp"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"MessageQuery_until": _message_query_until_model_schema})

_message_query_window_model_schema = json.loads(
    r"""{
  "title" : "MessageQuery_window",
  "description" : "A duration expression. Will be evaluated vs `from`, `until` or the query execution date to get the actual time range",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/DurationWithUnit"
  }, {
    "$ref" : "#/components/schemas/SO8601Timestamp"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"MessageQuery_window": _message_query_window_model_schema})

_multiple_series_query_request_inner_model_schema = json.loads(
    r"""{
  "title" : "MultipleSeriesQueryRequest_inner",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/SeriesQueryRequest"
  }, {
    "$ref" : "#/components/schemas/SeriesQueryWithoutAggregatesRequest"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "MultipleSeriesQueryRequest_inner": _multiple_series_query_request_inner_model_schema
})

_object_data_model_schema = json.loads(
    r"""{
  "title" : "Object Data",
  "description" : "Event data stored only in the _Message Cache_.",
  "oneOf" : [ {
    "title" : "Object",
    "type" : "object"
  }, {
    "title" : "Array",
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/Measurements"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Object_Data": _object_data_model_schema})

_order_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "the order in which the data is returned",
  "default" : "ascending",
  "enum" : [ "ascending", "descending" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Order": _order_model_schema})

_post_series_for_resource_request_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/Event"
  }, {
    "$ref" : "#/components/schemas/Events"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "postSeriesForResource_request": _post_series_for_resource_request_model_schema
})

_post_series_request_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/ResourceEvent"
  }, {
    "$ref" : "#/components/schemas/ResourceEvents"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"postSeries_request": _post_series_request_model_schema})

_publish_event_response_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "content" : {
      "$ref" : "#/components/schemas/PublishEventResponse_content"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PublishEventResponse": _publish_event_response_model_schema})

_publish_event_response_content_model_schema = json.loads(
    r"""{
  "title" : "PublishEventResponse_content",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/TimestampedResourceEvent"
  }, {
    "$ref" : "#/components/schemas/TimestampedResourceEvents"
  }, {
    "$ref" : "#/components/schemas/PublishEventResponse_content_anyOf"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PublishEventResponse_content": _publish_event_response_content_model_schema
})

_publish_event_response_content_any_of_model_schema = json.loads(
    r"""{
  "type" : "object",
  "description" : "Marks that multiple events where published",
  "enum" : [ { } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PublishEventResponse_content_anyOf": _publish_event_response_content_any_of_model_schema
})

_publish_resource_event_response_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "content" : {
      "$ref" : "#/components/schemas/PublishResourceEventResponse_content"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PublishResourceEventResponse": _publish_resource_event_response_model_schema
})

_publish_resource_event_response_content_model_schema = json.loads(
    r"""{
  "title" : "PublishResourceEventResponse_content",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/TimestampedEvent"
  }, {
    "$ref" : "#/components/schemas/PublishEventResponse_content_anyOf"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PublishResourceEventResponse_content": _publish_resource_event_response_content_model_schema
})

_query_time_series_200_response_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/TimeseriesJsonResult"
  }, {
    "$ref" : "#/components/schemas/MultipleTimeseriesJsonResult"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "queryTimeSeries_200_response": _query_time_series_200_response_model_schema
})

_query_time_series_request_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/SeriesQueryRequest"
  }, {
    "$ref" : "#/components/schemas/SeriesQueryWithoutAggregatesRequest"
  }, {
    "$ref" : "#/components/schemas/MultipleSeriesQueryRequest"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "queryTimeSeries_request": _query_time_series_request_model_schema
})

_resource_event_model_schema = json.loads(
    r"""{
  "required" : [ "resource" ],
  "type" : "object",
  "properties" : {
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "timestamp" : {
      "$ref" : "#/components/schemas/Event_timestamp"
    }
  },
  "additionalProperties" : {
    "$ref" : "#/components/schemas/Measurements"
  },
  "description" : "Measurement object with resource identifier and optional timestamp."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceEvent": _resource_event_model_schema})

_scalar_data_model_schema = json.loads(
    r"""{
  "title" : "ScalarData",
  "description" : "Event data stored in both the _Message Cache_ and _Time Series Database_.\nKeys of these measurements become a _Metric_ for the resource.",
  "nullable" : true,
  "oneOf" : [ {
    "title" : "Number",
    "type" : "number"
  }, {
    "title" : "String",
    "type" : "string"
  }, {
    "title" : "Boolean",
    "type" : "boolean"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ScalarData": _scalar_data_model_schema})

_series_key_value_inner_model_schema = json.loads(
    r"""{
  "title" : "SeriesKeyValue_inner",
  "nullable" : true,
  "oneOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/ScalarData"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesKeyValue_inner": _series_key_value_inner_model_schema})

_series_query_request_model_schema = json.loads(
    r"""{
  "required" : [ "aggregates", "metric", "resources" ],
  "type" : "object",
  "properties" : {
    "from" : {
      "$ref" : "#/components/schemas/SeriesQueryRequest_from"
    },
    "until" : {
      "$ref" : "#/components/schemas/SeriesQueryRequest_from"
    },
    "window" : {
      "$ref" : "#/components/schemas/SeriesQueryRequest_window"
    },
    "metric" : {
      "$ref" : "#/components/schemas/MetricId"
    },
    "aggregates" : {
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Aggregate"
      }
    },
    "grouping" : {
      "$ref" : "#/components/schemas/Grouping"
    },
    "resources" : {
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/ResourceId"
      }
    },
    "maxResults" : {
      "minimum" : 0,
      "type" : "integer"
    },
    "filter" : {
      "$ref" : "#/components/schemas/TimeseriesFilter"
    },
    "order" : {
      "$ref" : "#/components/schemas/Order"
    },
    "returnIngestionTimestamp" : {
      "$ref" : "#/components/schemas/ReturnIngestionTimestamp"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesQueryRequest": _series_query_request_model_schema})

_series_query_request_from_model_schema = json.loads(
    r"""{
  "title" : "SeriesQueryRequest_from",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/SO8601Timestamp"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "SeriesQueryRequest_from": _series_query_request_from_model_schema
})

_series_query_request_window_model_schema = json.loads(
    r"""{
  "title" : "SeriesQueryRequest_window",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/DurationWithUnit"
  }, {
    "$ref" : "#/components/schemas/SO8601Duration"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "SeriesQueryRequest_window": _series_query_request_window_model_schema
})

_series_query_response_model_schema = json.loads(
    r"""{
  "required" : [ "grouping", "metric", "resources" ],
  "type" : "object",
  "properties" : {
    "from" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    },
    "until" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    },
    "metric" : {
      "$ref" : "#/components/schemas/MetricId"
    },
    "aggregates" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Aggregate"
      }
    },
    "grouping" : {
      "$ref" : "#/components/schemas/Grouping"
    },
    "resources" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/ResourceId"
      }
    },
    "filter" : {
      "$ref" : "#/components/schemas/TimeseriesFilter"
    },
    "limit" : {
      "minimum" : 1,
      "type" : "integer"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesQueryResponse": _series_query_response_model_schema})

_series_query_without_aggregates_request_model_schema = json.loads(
    r"""{
  "required" : [ "metric", "resources" ],
  "type" : "object",
  "properties" : {
    "from" : {
      "$ref" : "#/components/schemas/SeriesQueryRequest_from"
    },
    "until" : {
      "$ref" : "#/components/schemas/SeriesQueryRequest_from"
    },
    "window" : {
      "$ref" : "#/components/schemas/SeriesQueryRequest_window"
    },
    "metric" : {
      "$ref" : "#/components/schemas/MetricId"
    },
    "aggregates" : {
      "maxItems" : 0,
      "minItems" : 0,
      "type" : "array",
      "items" : { }
    },
    "resources" : {
      "maxItems" : 1,
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/ResourceId"
      }
    },
    "maxResults" : {
      "minimum" : 0,
      "type" : "integer"
    },
    "filter" : {
      "$ref" : "#/components/schemas/TimeseriesFilter"
    },
    "order" : {
      "$ref" : "#/components/schemas/Order"
    },
    "returnIngestionTimestamp" : {
      "$ref" : "#/components/schemas/ReturnIngestionTimestamp"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "SeriesQueryWithoutAggregatesRequest": _series_query_without_aggregates_request_model_schema
})

_ttl_duration_model_schema = json.loads(
    r"""{
  "description" : "Specifies the duration of a TTL interval.",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/DurationSeconds"
  }, {
    "$ref" : "#/components/schemas/DurationWithUnit"
  }, {
    "$ref" : "#/components/schemas/SO8601Duration"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TTLDuration": _ttl_duration_model_schema})

_timeseries_filter_model_schema = json.loads(
    r"""{
  "title" : "TimeseriesFilter",
  "description" : "Filter that will be applied to datapoints *before* aggregation is performed.",
  "allOf" : [ {
    "$ref" : "#/components/schemas/TimeseriesFilterOperator"
  }, {
    "$ref" : "#/components/schemas/TimeseriesFilterValue"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TimeseriesFilter": _timeseries_filter_model_schema})

_timeseries_filter_operator_model_schema = json.loads(
    r"""{
  "required" : [ "operator" ],
  "type" : "object",
  "properties" : {
    "operator" : {
      "$ref" : "#/components/schemas/TimeseriesFilterOperator_operator"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TimeseriesFilterOperator": _timeseries_filter_operator_model_schema
})

_timeseries_filter_operator_operator_model_schema = json.loads(
    r"""{
  "title" : "TimeseriesFilterOperator_operator",
  "type" : "string",
  "enum" : [ "gt", "gte", "lt", "lte", "eq", "ne", "between" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TimeseriesFilterOperator_operator": _timeseries_filter_operator_operator_model_schema
})

_timeseries_filter_value_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/TimeseriesFilterValueExact"
  }, {
    "$ref" : "#/components/schemas/TimeseriesFilterValueBounds"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TimeseriesFilterValue": _timeseries_filter_value_model_schema
})

_timeseries_filter_value_bounds_model_schema = json.loads(
    r"""{
  "required" : [ "lowerBound", "upperBound" ],
  "type" : "object",
  "properties" : {
    "lowerBound" : {
      "type" : "number"
    },
    "upperBound" : {
      "type" : "number"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TimeseriesFilterValueBounds": _timeseries_filter_value_bounds_model_schema
})

_timeseries_filter_value_exact_model_schema = json.loads(
    r"""{
  "required" : [ "value" ],
  "type" : "object",
  "properties" : {
    "value" : {
      "$ref" : "#/components/schemas/TimeseriesFilterValueExact_value"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TimeseriesFilterValueExact": _timeseries_filter_value_exact_model_schema
})

_timeseries_filter_value_exact_value_model_schema = json.loads(
    r"""{
  "title" : "TimeseriesFilterValueExact_value",
  "oneOf" : [ {
    "type" : "number"
  }, {
    "type" : "string"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TimeseriesFilterValueExact_value": _timeseries_filter_value_exact_value_model_schema
})

_timeseries_json_result_model_schema = json.loads(
    r"""{
  "required" : [ "query", "series" ],
  "type" : "object",
  "properties" : {
    "query" : {
      "$ref" : "#/components/schemas/SeriesQueryResponse"
    },
    "series" : {
      "type" : "array",
      "description" : "Array of timestamp-value tuples",
      "items" : {
        "$ref" : "#/components/schemas/SeriesKeyValue"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TimeseriesJsonResult": _timeseries_json_result_model_schema})

_timestamped_event_model_schema = json.loads(
    r"""{
  "required" : [ "timestamp" ],
  "type" : "object",
  "properties" : {
    "timestamp" : {
      "description" : "Event timestamp",
      "allOf" : [ {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      } ]
    }
  },
  "additionalProperties" : {
    "$ref" : "#/components/schemas/Measurements"
  },
  "description" : "Measurement object with timestamp"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TimestampedEvent": _timestamped_event_model_schema})

_timestamped_resource_event_model_schema = json.loads(
    r"""{
  "required" : [ "resource", "timestamp" ],
  "type" : "object",
  "properties" : {
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "timestamp" : {
      "description" : "Event timestamp",
      "allOf" : [ {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      } ]
    }
  },
  "additionalProperties" : {
    "$ref" : "#/components/schemas/Measurements"
  },
  "description" : "Measurement object with resource identifier and timestamp."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TimestampedResourceEvent": _timestamped_resource_event_model_schema
})

_version_response_model_schema = json.loads(
    r"""{
  "required" : [ "name", "version" ],
  "type" : "object",
  "properties" : {
    "version" : {
      "type" : "string",
      "example" : "2.10.4"
    },
    "name" : {
      "type" : "string",
      "example" : "waylay-broker"
    },
    "message" : {
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VersionResponse": _version_response_model_schema})
