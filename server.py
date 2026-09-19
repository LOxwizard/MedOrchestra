from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pipeline import MedicalOrchestrator
from schema import CompleteMedicalReport

app = FastAPI(title="MedOrchestra AI API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = MedicalOrchestrator()

class TriageRequest(BaseModel):
    symptoms: str

@app.get("/api/health")
def health_check():
    return {"status": "online", "model": "llama3.2:1b"}

@app.post("/api/triage", response_model=CompleteMedicalReport)
def run_triage(request: TriageRequest):
    if not request.symptoms.strip():
        raise HTTPException(status_code=400, detail="Symptoms text cannot be empty.")
    
    try:
        report = orchestrator.process_case(request.symptoms)
        return report
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))