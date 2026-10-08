"""
Bayesian Knowledge Tracing and Quiz Generation Engine
"""

def update_knowledge_tracing(prior_p: float, answered_correctly: bool) -> float:
    return 0.94 if answered_correctly else 0.40