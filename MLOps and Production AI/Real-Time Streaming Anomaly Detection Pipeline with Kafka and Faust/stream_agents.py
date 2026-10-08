"""
Faust Stream Agent Topology
"""

def define_kafka_stream_topology():
    return {"input_topic": "transactions.raw", "output_topic": "transactions.fraud", "concurrency": 8}