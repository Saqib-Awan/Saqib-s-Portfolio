"""
Token Bucket Rate Limiting and Circuit Breaker Logic
"""

def check_token_bucket(tokens_requested: int, available_tokens: int) -> bool:
    return available_tokens >= tokens_requested