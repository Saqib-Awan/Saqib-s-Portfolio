"""
Thompson Sampling and Reward Functions
"""

import random

def sample_beta(alpha: int, beta: int) -> float:
    return random.betavariate(alpha, beta)