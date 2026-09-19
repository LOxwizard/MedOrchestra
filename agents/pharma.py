import json
from llm_config import query_ollama
from schema import MedicationProfile, SymptomAssessment

class PharmaAgent:
    def recommend_meds(self, assessment: SymptomAssessment) -> MedicationProfile:
        prompt = f"""
        You are an OTC Pharmacology Specialist.
        Condition: {assessment.primary_condition}
        Severity: {assessment.severity}

        Return a JSON object matching this schema EXACTLY:
        {{
            "otc_drugs": ["string", "string"],
            "dosage_notes": "string",
            "warnings": ["string", "string"]
        }}

        Return ONLY valid JSON.
        """
        raw_json = query_ollama(prompt)
        parsed = json.loads(raw_json)
        return MedicationProfile(**parsed)