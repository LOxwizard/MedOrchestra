from pydantic import BaseModel, Field
from typing import List, Optional

class SymptomAssessment(BaseModel):
    primary_condition: str = Field(description="Most likely condition or illness")
    severity: str = Field(description="Low, Moderate, or Severe")
    key_observations: List[str] = Field(description="Key observations from symptoms")

class RecoveryPlan(BaseModel):
    home_remedies: List[str] = Field(description="Non-medical steps for recovery")
    lifestyle_tips: List[str] = Field(description="Rest, hydration, and diet recommendations")

class MedicationProfile(BaseModel):
    otc_drugs: List[str] = Field(description="Common over-the-counter medications")
    dosage_notes: str = Field(description="General guidance on usage")
    warnings: List[str] = Field(description="Crucial precautions and when to see a doctor")

class CompleteMedicalReport(BaseModel):
    patient_query: str
    assessment: SymptomAssessment
    recovery: RecoveryPlan
    medication: MedicationProfile