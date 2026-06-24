from fastapi import APIRouter, HTTPException, status

from app.core.security import hash_prompt
from app.schemas.workflow import UnsupportedStateResponse, WorkflowRequest, WorkflowResponse
from app.services.intent import IntentExtractionError, extract_goal_key
from app.services.seed_data import SUPPORTED_STATES
from app.services.workflow_graph import build_workflow

router = APIRouter(prefix="/workflows", tags=["workflows"])


@router.post("", response_model=WorkflowResponse | UnsupportedStateResponse)
def generate_workflow(payload: WorkflowRequest) -> WorkflowResponse | UnsupportedStateResponse:
    if payload.state_code not in SUPPORTED_STATES:
        state = next(iter(SUPPORTED_STATES.values()))
        return UnsupportedStateResponse(
            message=(
                f"ProcessIQ currently supports {state['name']} workflows. "
                f"Support for {', '.join(state['planned'])} and other states is planned."
            ),
            supported_state_codes=list(SUPPORTED_STATES.keys()),
            planned_states=state["planned"]
        )

    try:
        goal_key = extract_goal_key(payload.goal)
    except IntentExtractionError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Please clarify the civic goal, location, and core activity."
        ) from exc

    return build_workflow(goal_key=goal_key, prompt_hash=hash_prompt(payload.goal))
