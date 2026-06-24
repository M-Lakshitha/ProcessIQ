from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ProcessIQ API"
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/processiq"
    jwt_secret: str = "change-me"
    prompt_retention_days: int = 30
    primary_llm: str = "qwen3:8b"
    fallback_llm: str = "gemma3:12b"
    ollama_base_url: str = "http://localhost:11434"
    llm_timeout_seconds: float = 8.0

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
