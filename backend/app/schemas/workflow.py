from pydantic import BaseModel, Field, HttpUrl


class WorkflowRequest(BaseModel):
    goal: str = Field(min_length=2, max_length=240)
    state_code: str = Field(default="TN", min_length=2, max_length=8)
    attributes: dict[str, str | int | float | bool] = Field(default_factory=dict)


class ServiceCard(BaseModel):
    id: str
    name: str
    department: str
    approximate_cost: str
    processing_time: str
    official_url: HttpUrl
    source_document: str
    last_verified: str
    version: str
    applicable_state: str


class Phase(BaseModel):
    id: str
    title: str
    services: list[ServiceCard]


class WorkflowResponse(BaseModel):
    goal_detected: str
    category: str
    timeline: str
    phases: list[Phase]
    prompt_hash: str
    disclaimer: str


class UnsupportedStateResponse(BaseModel):
    message: str
    supported_state_codes: list[str]
    planned_states: list[str]
