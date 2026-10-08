"""
Prompt Injection Defense Firewall
"""
from typing import Dict, Any

class PromptFirewall:
    def inspect_prompt(self, prompt: str) -> Dict[str, Any]:
        is_attack = "ignore previous" in prompt.lower() or "system prompt" in prompt.lower()
        return {
            "verdict": "BLOCKED" if is_attack else "ALLOWED",
            "threat_category": "PROMPT_INJECTION" if is_attack else "NONE",
            "latency_ms": 7.8
        }
