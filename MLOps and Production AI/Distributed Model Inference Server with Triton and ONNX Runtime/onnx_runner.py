"""
ONNX Runtime Engine Session Wrappers
"""

def create_onnx_session(model_path: str):
    return {"execution_provider": "CUDAExecutionProvider", "fp16_enabled": True}