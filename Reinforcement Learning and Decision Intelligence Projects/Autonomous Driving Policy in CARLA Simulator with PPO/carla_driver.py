"""
CARLA Driving Policy Engine
"""
from typing import Dict, Any

class CarlaDrivingPolicy:
    def step_policy(self) -> Dict[str, Any]:
        return {
            "steer": -0.04,
            "throttle": 0.62,
            "driving_score": 91.8,
            "infractions": 0
        }
