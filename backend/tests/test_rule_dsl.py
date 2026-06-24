import pytest

from app.services.rule_dsl import Rule, RuleConflictError, apply_rules, evaluate_expression


def test_rule_dsl_supports_and_and_numeric_comparisons() -> None:
    assert evaluate_expression(
        "business=bakery AND seating_capacity>20",
        {"business": "bakery", "seating_capacity": 35}
    )


def test_rule_priorities_and_future_states() -> None:
    rules = [
        Rule(id="future", expression="ownership=inherited", service_ids=("future_service",), priority=1, future_state=True),
        Rule(id="active", expression="ownership=inherited", service_ids=("patta",), priority=10)
    ]
    assert apply_rules(rules, {"ownership": "inherited"}) == ["patta"]


def test_conflict_detection() -> None:
    rules = [
        Rule(id="a", expression="ownership=inherited", service_ids=("patta",), priority=1),
        Rule(id="b", expression="ownership=inherited", service_ids=("ec",), priority=1)
    ]
    with pytest.raises(RuleConflictError):
        apply_rules(rules, {"ownership": "inherited"})
