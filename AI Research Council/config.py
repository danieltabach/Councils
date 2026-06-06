from dataclasses import dataclass

MODEL_OPUS = "claude-opus-4-7"
MODEL_SONNET = "claude-sonnet-4-6"

@dataclass
class PersonaConfig:
    name: str
    slug: str
    model: str
    stage1_temp: float = 0.7
    stage2_temp: float = 0.5
    max_tokens_review: int = 4096
    max_tokens_deliberation: int = 2048


REVIEWERS: list[PersonaConfig] = [
    PersonaConfig(name="Source Auditor", slug="source_auditor", model=MODEL_SONNET),
    PersonaConfig(name="Methodologist", slug="methodologist", model=MODEL_SONNET),
    PersonaConfig(name="Peer Reviewer", slug="peer_reviewer", model=MODEL_SONNET),
    PersonaConfig(name="Domain Expert", slug="domain_expert", model=MODEL_SONNET),
    PersonaConfig(name="Outsider / Red Team", slug="outsider", model=MODEL_SONNET),
    PersonaConfig(name="Alignment Guide", slug="alignment_guide", model=MODEL_SONNET),
]

CHAIRMAN_MODEL = MODEL_OPUS
CHAIRMAN_TEMP = 0.3
CHAIRMAN_MAX_TOKENS = 8192

MAX_CONCURRENT_REQUESTS = 6

PRICING: dict[str, dict[str, float]] = {
    MODEL_OPUS: {
        "input": 15.0,
        "output": 75.0,
        "cache_read": 1.5,
        "cache_create": 18.75,
    },
    MODEL_SONNET: {
        "input": 3.0,
        "output": 15.0,
        "cache_read": 0.30,
        "cache_create": 3.75,
    },
}
