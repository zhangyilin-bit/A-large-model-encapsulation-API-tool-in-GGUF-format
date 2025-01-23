from fastapi import FastAPI
from pydantic import BaseModel
from model_loader import load_model, generate

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 100
    temperature: float = 0.7

@app.post("/generate")
async def generate_text(request: PromptRequest):
    model = load_model()
    output = generate(model, request.prompt, request.max_tokens, request.temperature)
    return {"response": output}
