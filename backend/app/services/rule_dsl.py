from __future__ import annotations

from dataclasses import dataclass
import operator
import re
from typing import Any, Callable


OPS: dict[str, Callable[[Any, Any], bool]] = {
    "=": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    ">=": operator.ge,
    "<": operator.lt,
    "<=": operator.le
}


@dataclass(frozen=True)
class Rule:
    id: str
    expression: str
    service_ids: tuple[str, ...]
    priority: int = 100
    future_state: bool = False


class RuleConflictError(ValueError):
    pass


def evaluate_expression(expression: str, attributes: dict[str, Any]) -> bool:
    clauses = [clause.strip() for clause in re.split(r"\bAND\b", expression, flags=re.IGNORECASE)]
    return all(_evaluate_clause(clause, attributes) for clause in clauses if clause)


def detect_conflicts(rules: list[Rule]) -> list[tuple[str, str]]:
    by_priority: dict[int, list[Rule]] = {}
    for rule in rules:
        by_priority.setdefault(rule.priority, []).append(rule)

    conflicts: list[tuple[str, str]] = []
    for same_priority_rules in by_priority.values():
        seen: dict[str, str] = {}
        for rule in same_priority_rules:
            normalized = _normalize_expression(rule.expression)
            if normalized in seen and seen[normalized] != ",".join(rule.service_ids):
                conflicts.append((seen[normalized], rule.id))
            seen[normalized] = rule.id
    return conflicts


def apply_rules(rules: list[Rule], attributes: dict[str, Any]) -> list[str]:
    conflicts = detect_conflicts(rules)
    if conflicts:
        formatted = ", ".join(f"{left}/{right}" for left, right in conflicts)
        raise RuleConflictError(f"Conflicting rules: {formatted}")

    selected: list[str] = []
    for rule in sorted(rules, key=lambda item: item.priority):
        if not rule.future_state and evaluate_expression(rule.expression, attributes):
            selected.extend(rule.service_ids)
    return selected


def _evaluate_clause(clause: str, attributes: dict[str, Any]) -> bool:
    match = re.fullmatch(r"([a-zA-Z_][\w]*)\s*(=|!=|>=|<=|>|<)\s*([\w.-]+)", clause)
    if not match:
        raise ValueError(f"Invalid rule clause: {clause}")

    key, op, raw_expected = match.groups()
    actual = attributes.get(key)
    expected = _coerce(raw_expected)
    actual = _coerce(actual)

    if actual is None:
        return False
    return OPS[op](actual, expected)


def _coerce(value: Any) -> Any:
    if value is None or isinstance(value, (int, float, bool)):
        return value
    text = str(value).strip()
    if re.fullmatch(r"-?\d+", text):
        return int(text)
    if re.fullmatch(r"-?\d+\.\d+", text):
        return float(text)
    if text.lower() in {"true", "false"}:
        return text.lower() == "true"
    return text.lower()


def _normalize_expression(expression: str) -> str:
    clauses = sorted(clause.strip().lower() for clause in re.split(r"\bAND\b", expression, flags=re.IGNORECASE))
    return " AND ".join(clauses)
