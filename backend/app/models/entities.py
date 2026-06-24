from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class IdMixin:
    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid4()))


class State(IdMixin, TimestampMixin, Base):
    __tablename__ = "states"
    code: Mapped[str] = mapped_column(String(8), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    is_supported: Mapped[bool] = mapped_column(Boolean, default=False)


class Category(IdMixin, TimestampMixin, Base):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(String(160), unique=True)


class Goal(IdMixin, TimestampMixin, Base):
    __tablename__ = "goals"
    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"))
    canonical_name: Mapped[str] = mapped_column(String(160))
    patterns: Mapped[dict] = mapped_column(JSONB, default=dict)


class Attribute(IdMixin, TimestampMixin, Base):
    __tablename__ = "attributes"
    key: Mapped[str] = mapped_column(String(120), unique=True)
    value_type: Mapped[str] = mapped_column(String(40))


class Department(IdMixin, TimestampMixin, Base):
    __tablename__ = "departments"
    name: Mapped[str] = mapped_column(String(180), unique=True)
    state_id: Mapped[str | None] = mapped_column(ForeignKey("states.id"), nullable=True)


class Service(IdMixin, TimestampMixin, Base):
    __tablename__ = "services"
    department_id: Mapped[str] = mapped_column(ForeignKey("departments.id"))
    state_id: Mapped[str] = mapped_column(ForeignKey("states.id"))
    name: Mapped[str] = mapped_column(String(220))
    official_url: Mapped[str] = mapped_column(Text)
    approximate_cost: Mapped[str] = mapped_column(String(160))
    processing_time: Mapped[str] = mapped_column(String(160))
    version: Mapped[str] = mapped_column(String(40))
    last_verified_at: Mapped[datetime] = mapped_column(DateTime)


class Rule(IdMixin, TimestampMixin, Base):
    __tablename__ = "rules"
    goal_id: Mapped[str] = mapped_column(ForeignKey("goals.id"))
    expression: Mapped[str] = mapped_column(Text)
    priority: Mapped[int] = mapped_column(Integer, default=100)
    service_ids: Mapped[dict] = mapped_column(JSONB, default=dict)
    future_state: Mapped[bool] = mapped_column(Boolean, default=False)


class Dependency(IdMixin, TimestampMixin, Base):
    __tablename__ = "dependencies"
    upstream_service_id: Mapped[str] = mapped_column(ForeignKey("services.id"))
    downstream_service_id: Mapped[str] = mapped_column(ForeignKey("services.id"))
    __table_args__ = (UniqueConstraint("upstream_service_id", "downstream_service_id"),)


class ClarificationQuestion(IdMixin, TimestampMixin, Base):
    __tablename__ = "clarification_questions"
    goal_id: Mapped[str] = mapped_column(ForeignKey("goals.id"))
    question: Mapped[str] = mapped_column(Text)


class RelatedService(IdMixin, TimestampMixin, Base):
    __tablename__ = "related_services"
    service_id: Mapped[str] = mapped_column(ForeignKey("services.id"))
    related_service_id: Mapped[str] = mapped_column(ForeignKey("services.id"))


class ServiceProvenance(IdMixin, TimestampMixin, Base):
    __tablename__ = "service_provenance"
    service_id: Mapped[str] = mapped_column(ForeignKey("services.id"))
    source_url: Mapped[str] = mapped_column(Text)
    source_document: Mapped[str] = mapped_column(Text)
    parser_model: Mapped[str | None] = mapped_column(String(80), nullable=True)


class FeatureFlag(IdMixin, TimestampMixin, Base):
    __tablename__ = "feature_flags"
    key: Mapped[str] = mapped_column(String(120), unique=True)
    enabled: Mapped[bool] = mapped_column(Boolean, default=False)


class PendingService(IdMixin, TimestampMixin, Base):
    __tablename__ = "pending_services"
    payload: Mapped[dict] = mapped_column(JSONB)
    source_url: Mapped[str] = mapped_column(Text)
    approved: Mapped[bool] = mapped_column(Boolean, default=False)


class PendingRule(IdMixin, TimestampMixin, Base):
    __tablename__ = "pending_rules"
    payload: Mapped[dict] = mapped_column(JSONB)
    approved: Mapped[bool] = mapped_column(Boolean, default=False)


class Feedback(IdMixin, TimestampMixin, Base):
    __tablename__ = "feedback"
    prompt_hash: Mapped[str] = mapped_column(String(64), index=True)
    rating: Mapped[int | None] = mapped_column(Integer, nullable=True)
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)


class PromptVersion(IdMixin, TimestampMixin, Base):
    __tablename__ = "prompt_versions"
    prompt: Mapped[str] = mapped_column(Text)
    model: Mapped[str] = mapped_column(String(80))
    version: Mapped[str] = mapped_column(String(40))
    accuracy: Mapped[int | None] = mapped_column(Integer, nullable=True)


class EvaluationResult(IdMixin, TimestampMixin, Base):
    __tablename__ = "evaluation_results"
    prompt_version_id: Mapped[str] = mapped_column(ForeignKey("prompt_versions.id"))
    metric: Mapped[str] = mapped_column(String(120))
    score: Mapped[int] = mapped_column(Integer)


class AdminUser(IdMixin, TimestampMixin, Base):
    __tablename__ = "admin_users"
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(Text)


class AuditLog(IdMixin, TimestampMixin, Base):
    __tablename__ = "audit_logs"
    actor_id: Mapped[str | None] = mapped_column(ForeignKey("admin_users.id"), nullable=True)
    action: Mapped[str] = mapped_column(String(160))
    payload: Mapped[dict] = mapped_column(JSONB, default=dict)


class SearchAnalytic(IdMixin, TimestampMixin, Base):
    __tablename__ = "search_analytics"
    prompt_hash: Mapped[str] = mapped_column(String(64), index=True)
    state_code: Mapped[str] = mapped_column(String(8))
    matched_goal_id: Mapped[str | None] = mapped_column(ForeignKey("goals.id"), nullable=True)
