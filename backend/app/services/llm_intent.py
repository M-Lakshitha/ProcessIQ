import json
from typing import Protocol

import httpx

from app.core.config import settings
from app.services.seed_data import GOALS


class LlmIntentError(ValueError):
    pass


class LlmClient(Protocol):
    def detect_goal(self, prompt: str, model: str) -> str:
        pass


class OllamaIntentClient:
    def __init__(self, base_url: str = settings.ollama_base_url, timeout: float = settings.llm_timeout_seconds):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def detect_goal(self, prompt: str, model: str) -> str:
        response = httpx.post(
            f"{self.base_url}/api/generate",
            json={
                "model": model,
                "prompt": build_intent_prompt(prompt),
                "stream": False,
                "format": "json"
            },
            timeout=self.timeout
        )
        response.raise_for_status()
        raw = response.json().get("response", "")
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise LlmIntentError("LLM returned invalid JSON") from exc

        goal_key = parsed.get("goal_key")
        if not isinstance(goal_key, str) or goal_key not in GOALS:
            raise LlmIntentError("LLM returned an unknown goal")
        return goal_key


def build_intent_prompt(prompt: str) -> str:
    goal_lines = "\n".join(
        f"- {key}: {goal['goal']} ({goal['category']})"
        for key, goal in sorted(GOALS.items())
    )
    return (
        "You classify civic workflow intent for ProcessIQ.\n"
        "Return JSON only, with this exact shape: {\"goal_key\":\"<one_known_goal_key>\"}.\n"
        "Choose only from the known goal keys below. Do not invent workflows, services, legal advice, "
        "eligibility decisions, document validation, or application outcomes.\n\n"
        f"Known goals:\n{goal_lines}\n\n"
        f"User goal: {prompt}"
    )


def detect_goal_with_llms(prompt: str, client: LlmClient | None = None) -> str:
    llm_client = client or OllamaIntentClient()
    errors: list[Exception] = []

    for model in (settings.primary_llm, settings.fallback_llm):
        try:
            return llm_client.detect_goal(prompt, model)
        except Exception as exc:
            errors.append(exc)

    raise LlmIntentError("LLM intent extraction failed") from errors[-1]
