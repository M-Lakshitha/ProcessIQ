import re

from app.services.llm_intent import LlmClient, LlmIntentError, detect_goal_with_llms
from app.services.seed_data import GOALS


class IntentExtractionError(ValueError):
    pass


def extract_goal_key(prompt: str, llm_client: LlmClient | None = None) -> str:
    try:
        return extract_goal_key_regex(prompt)
    except IntentExtractionError:
        pass

    try:
        return detect_goal_with_llms(prompt, client=llm_client)
    except LlmIntentError as exc:
        raise IntentExtractionError("Clarification required") from exc


def extract_goal_key_regex(prompt: str) -> str:
    normalized = prompt.strip().lower()
    for key, goal in GOALS.items():
        if any(re.search(pattern, normalized) for pattern in goal["patterns"]):
            return key
    raise IntentExtractionError("Clarification required")
