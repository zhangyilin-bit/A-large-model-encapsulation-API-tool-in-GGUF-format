from llama_cpp import Llama
from typing import Optional
import os

MODEL_PATH = "/home/ai/workspace/zyl_workspace/Ollama/data/Qwen2.5-0.5B-train/Qwen2.5-0.5B-train-F16.gguf"

_model_instance = None

def load_model():
    global _model_instance
    if _model_instance is None:
        _model_instance = Llama(
            model_path=MODEL_PATH,
            n_ctx=2048,
            n_threads=4,
            n_gpu_layers=0
        )
    return _model_instance

def generate(model, prompt: str, max_tokens: int = 100, temperature: float = 0.7) -> str:
    output = model.create_completion(
        prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        stop=["\n", "。", "！", "？"]
    )
    return output["choices"][0]["text"]
