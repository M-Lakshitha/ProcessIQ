import pytest

from app.services.workflow_graph import WorkflowGraphError, build_workflow, parallel_groups


def test_build_house_parallel_phases() -> None:
    workflow = build_workflow("build_house", prompt_hash="abc")
    assert workflow.goal_detected == "Build House"
    assert [service.id for service in workflow.phases[0].services] == ["ec", "patta", "survey"]
    assert workflow.phases[1].services[0].id == "building-approval"
    assert {service.id for service in workflow.phases[2].services} == {"electricity", "water"}


def test_parallel_group_helper() -> None:
    groups = parallel_groups("build_house")
    assert groups[0] == ["ec", "patta", "survey"]


def test_cycle_detection(monkeypatch: pytest.MonkeyPatch) -> None:
    from app.services import seed_data

    original = seed_data.GOALS["build_house"]["dependencies"]
    monkeypatch.setitem(
        seed_data.GOALS["build_house"],
        "dependencies",
        [*original, ("electricity", "patta")]
    )
    with pytest.raises(WorkflowGraphError):
        build_workflow("build_house", prompt_hash="abc")
