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
    web_search: bool = False


REVIEWERS: list[PersonaConfig] = [
    PersonaConfig(name="Field Cartographer", slug="field_cartographer", model=MODEL_SONNET, web_search=True),
    PersonaConfig(name="Devil's Advocate", slug="devils_advocate", model=MODEL_SONNET),
    PersonaConfig(name="Research Sequencer", slug="research_sequencer", model=MODEL_SONNET),
    PersonaConfig(name="Alignment Insider", slug="alignment_insider", model=MODEL_SONNET, web_search=True),
    PersonaConfig(name="Career Strategist", slug="career_strategist", model=MODEL_SONNET),
    PersonaConfig(name="Skeptical PI", slug="skeptical_pi", model=MODEL_SONNET),
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
