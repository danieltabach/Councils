from dataclasses import dataclass

MODEL_OPUS = "claude-opus-4-8"
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
    PersonaConfig(name="Hiring Manager", slug="hiring_manager", model=MODEL_SONNET),
    PersonaConfig(name="Recruiter & ATS Lens", slug="recruiter_lens", model=MODEL_SONNET),
    PersonaConfig(name="Story Architect", slug="story_architect", model=MODEL_SONNET),
    PersonaConfig(name="Bullet Surgeon", slug="bullet_surgeon", model=MODEL_SONNET),
    PersonaConfig(name="Skeptical Interviewer", slug="skeptical_interviewer", model=MODEL_SONNET),
    PersonaConfig(name="Market Benchmarker", slug="market_benchmarker", model=MODEL_SONNET),
    PersonaConfig(name="Layout Strategist", slug="layout_strategist", model=MODEL_SONNET),
    PersonaConfig(name="Assembly Strategist", slug="assembly_strategist", model=MODEL_SONNET),
]

MAX_CONCURRENT_REQUESTS = 8

CHAIRMAN_MODEL = MODEL_OPUS
CHAIRMAN_TEMP = 0.3
CHAIRMAN_MAX_TOKENS = 8192

PRICING: dict[str, dict[str, float]] = {
    MODEL_OPUS: {
        "input": 5.0,
        "output": 25.0,
        "cache_read": 0.50,
        "cache_create": 6.25,
    },
    MODEL_SONNET: {
        "input": 3.0,
        "output": 15.0,
        "cache_read": 0.30,
        "cache_create": 3.75,
    },
}
