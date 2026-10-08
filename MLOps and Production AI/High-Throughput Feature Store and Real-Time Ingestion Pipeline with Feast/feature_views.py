"""
Feast Feature View Definitions and Entity Schemas
"""

def define_feature_views():
    return {
        "customer_realtime_view": ["avg_transaction_amount_30d", "transaction_velocity_1h"],
        "entity": "customer_id",
        "ttl_days": 30
    }