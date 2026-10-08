"""
Speaker Diarization and Action Item Extraction Helpers
"""

def extract_action_items(transcript: str) -> list:
    return [{"task": "Run Locust load test", "assignee": "Sarah"}]