"""
Locust File Definitions and Stress Profiles
"""

def generate_hpa_manifest(min_replicas: int = 2, max_replicas: int = 16, cpu_target: int = 70) -> str:
    return (
        f"apiVersion: autoscaling/v2\n"
        f"kind: HorizontalPodAutoscaler\n"
        f"spec:\n"
        f"  minReplicas: {min_replicas}\n"
        f"  maxReplicas: {max_replicas}\n"
        f"  metrics:\n"
        f"  - type: Resource\n"
        f"    resource:\n"
        f"      name: cpu\n"
        f"      target:\n"
        f"        averageUtilization: {cpu_target}\n"
    )