# (C) 2021 GoodData Corporation
from __future__ import annotations

import json
import os

import pytest

from gooddata_sdk.compute_model import (
    AbsoluteDateFilter,
    Attribute,
    ObjId,
    PopDate,
    PopDateDataset,
    PopDateMetric,
    PopDatesetMetric,
    PositiveAttributeFilter,
    SimpleMetric,
    compute_model_to_api_model,
)

_current_dir = os.path.dirname(os.path.abspath(__file__))


def _scenario_to_snapshot_name(scenario: str):
    return f"{scenario.replace(' ', '_')}.snapshot.json"


_simple_metric = SimpleMetric(local_id="simple_metric_local_id", item=ObjId(type="metric", id="metric_id"))
_attribute = Attribute(local_id="attribute_local_id", label="label.id")

_pop_dataset_metric = PopDatesetMetric(
    local_id="local_id1",
    metric=_simple_metric,
    date_datasets=[PopDateDataset(dataset=ObjId(type="dataset", id="dataset.id"), periods_ago=1)],
)

_pop_date_metric = PopDateMetric(
    local_id="local_id1",
    metric=_simple_metric,
    date_attributes=[PopDate(attribute=ObjId(type="label", id="label.id"), periods_ago=1)],
)

_positive_filter = PositiveAttributeFilter(label=_attribute, values=["val1", "val2"])

_absolute_date_filter = AbsoluteDateFilter(
    dataset=ObjId(type="dataset", id="dataset.id"),
    from_date="2021/1/1",
    to_date="2021/1/2",
)

test_inputs = [
    [
        "multiple attributes and metrics and filters",
        [_attribute, Attribute(local_id="attribute_local_id2", label="label2.id")],
        [_simple_metric, _pop_date_metric, _pop_dataset_metric],
        [_positive_filter, _absolute_date_filter],
    ],
    ["attribute only", [_attribute], None, None],
    ["attribute and filter ", [_attribute], None, [_positive_filter]],
    ["metric only ", None, [_simple_metric], None],
    ["metric and filter ", None, [_simple_metric], [_positive_filter]],
    [
        "attribute and metric and filter ",
        [_attribute],
        [_simple_metric],
        [_positive_filter],
    ],
]


@pytest.mark.parametrize("scenario,attributes,metrics,filters", test_inputs)
def test_attribute_filters_to_api_model(scenario, attributes, metrics, filters, snapshot):
    # it is essential to define snapshot dir using absolute path, otherwise snapshots cannot be found when
    # running in tox
    snapshot.snapshot_dir = os.path.join(_current_dir, "afm")

    afm = compute_model_to_api_model(attributes, metrics, filters)

    snapshot.assert_match(
        json.dumps(afm.to_dict(), indent=4, sort_keys=True),
        _scenario_to_snapshot_name(scenario),
    )
