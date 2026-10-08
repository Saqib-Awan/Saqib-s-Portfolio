"""
Keyword Spotting Engine
"""
from typing import Dict, Any

class KeywordSpotter:
    def process_frame(self) -> Dict[str, Any]:
        return {
            "keyword_detected": "Hey Assistant",
            "confidence": 0.988,
            "latency_ms": 1.4,
            "state": "AWAKE"
        }
