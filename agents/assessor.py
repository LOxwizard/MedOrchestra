import json
from llm_config import query_ollama
from schema import SymptomAssessment

class AssessorAgent:
    def evaluate(self, symptoms_text: str) -> SymptomAssessment:
        prompt = f"""
        You are a Clinical Diagnostic AI. 
        Analyze the patient's symptoms and return a JSON object matching this schema EXACTLY:
        {{
            "primary_condition": "string",
            "severity": "Low | Moderate | Severe",
            "key_observations": ["string", "string"]
        }}

        Patient Symptoms: {symptoms_text}
        Return ONLY valid JSON.
        """
        raw_json = query_ollama(prompt)
        parsed = json.loads(raw_json)
        return SymptomAssessment(**parsed)