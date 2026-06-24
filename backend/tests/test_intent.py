import pytest

from app.services.intent import IntentExtractionError, extract_goal_key, extract_goal_key_regex


class StubLlmClient:
    def __init__(self, responses: list[str | Exception]):
        self.responses = responses
        self.models: list[str] = []

    def detect_goal(self, prompt: str, model: str) -> str:
        self.models.append(model)
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response


def test_regex_runs_before_llm() -> None:
    client = StubLlmClient(["build_house"])
    assert extract_goal_key("Build House", llm_client=client) == "build_house"
    assert client.models == []


def test_llm_fallback_when_regex_fails() -> None:
    client = StubLlmClient(["open_bakery"])
    assert extract_goal_key("I want to run a small cake shop", llm_client=client) == "open_bakery"


def test_llm_primary_then_fallback() -> None:
    client = StubLlmClient([RuntimeError("qwen unavailable"), "sale_land"])
    assert extract_goal_key("transfer my plot to a buyer", llm_client=client) == "sale_land"
    assert client.models == ["qwen3:8b", "gemma3:12b"]


def test_clarification_when_regex_and_llms_fail() -> None:
    client = StubLlmClient([RuntimeError("qwen unavailable"), RuntimeError("gemma unavailable")])
    with pytest.raises(IntentExtractionError):
        extract_goal_key("something vague", llm_client=client)


def test_regex_can_be_tested_directly() -> None:
    assert extract_goal_key_regex("sell my land") == "sale_land"
