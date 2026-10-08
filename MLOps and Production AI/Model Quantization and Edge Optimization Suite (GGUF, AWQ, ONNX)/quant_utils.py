"""
AWQ and GGUF Quantization Engine Wrappers
"""

def estimate_vram_requirement(param_count_billions: float, bits_per_weight: int) -> float:
    return (param_count_billions * bits_per_weight) / 8.0 * 1.2