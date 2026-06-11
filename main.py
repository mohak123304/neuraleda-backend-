from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from eda_engine import NeuralEDAAgent  # Import custom runtime module

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LintRequest(BaseModel):
    code: str
    module_name: str = "neural_mod"

@app.post("/api/v1/lint")
async def process_lint(req: LintRequest):
    # Initialize our dynamic tracking agent
    agent = NeuralEDAAgent(code=req.code, module_name=req.module_name)
    results = agent.execute_pipeline()
    return {
        "status": "success",
        **results
    }
