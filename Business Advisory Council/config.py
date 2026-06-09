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
    PersonaConfig(name="Strategy Consultant", slug="strategy_consultant", model=MODEL_SONNET, web_search=True),
    PersonaConfig(name="Marketing Strategist", slug="marketing_strategist", model=MODEL_SONNET, web_search=True),
    PersonaConfig(name="Conversion Architect", slug="conversion_architect", model=MODEL_SONNET, web_search=True),
    PersonaConfig(name="The Customer", slug="the_customer", model=MODEL_SONNET, web_search=True),
    PersonaConfig(name="Market Analyst", slug="market_analyst", model=MODEL_SONNET, web_search=True),
    PersonaConfig(name="Business Evaluator", slug="business_evaluator", model=MODEL_SONNET, web_search=True),
    PersonaConfig(name="Creative Director", slug="creative_director", model=MODEL_SONNET, web_search=True),
    PersonaConfig(name="Future Visionary", slug="future_visionary", model=MODEL_SONNET, web_search=True),
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
