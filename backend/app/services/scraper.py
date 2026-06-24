from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from urllib.parse import urlparse

OFFICIAL_HOST_SUFFIXES = (
    ".tn.gov.in",
    "tn.gov.in",
    "tnreginet.gov.in",
    "eservices.tn.gov.in",
    "tnebltd.gov.in"
)


@dataclass(frozen=True)
class ScrapedService:
    service_name: str
    cost: str
    department: str
    processing_time: str
    dependencies: list[str]
    requirements: list[str]
    source_url: str
    scraped_at: datetime


def is_allowed_source(url: str) -> bool:
    host = urlparse(url).hostname or ""
    return any(host == suffix or host.endswith(suffix) for suffix in OFFICIAL_HOST_SUFFIXES)


async def scrape_service_page(url: str) -> ScrapedService:
    if not is_allowed_source(url):
        raise ValueError("Only official Tamil Nadu portal sources are allowed.")

    # Playwright navigation and Gemma3 parser invocation are intentionally isolated here.
    # The returned object is written to pending_services and must be approved by an admin.
    return ScrapedService(
        service_name="Pending parser extraction",
        cost="Pending parser extraction",
        department="Pending parser extraction",
        processing_time="Pending parser extraction",
        dependencies=[],
        requirements=[],
        source_url=url,
        scraped_at=datetime.now(UTC)
    )
