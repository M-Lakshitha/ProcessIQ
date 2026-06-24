import hashlib
from datetime import UTC, datetime, timedelta

from jose import jwt

from app.core.config import settings


def hash_prompt(prompt: str) -> str:
    return hashlib.sha256(prompt.strip().encode("utf-8")).hexdigest()


def create_access_token(subject: str, minutes: int = 60) -> str:
    expires_at = datetime.now(UTC) + timedelta(minutes=minutes)
    return jwt.encode({"sub": subject, "exp": expires_at}, settings.jwt_secret, algorithm="HS256")
