import json
from llm_config import query_ollama
from schema import RecoveryPlan, SymptomAssessment

class RemediesAgent:
    def suggest_care(self, assessment: SymptomAssessment) -> RecoveryPlan:
        prompt = f"""
        You are a Home Care Specialist.
        Condition: {assessment.primary_condition}
        Severity: {assessment.severity}

        Return a JSON object matching this schema EXACTLY:
        {{
            "home_remedies": ["string", "string"],
            "lifestyle_tips": ["string", "string"]
        }}

        Return ONLY valid JSON.
        """
        raw_json = query_ollama(prompt)
        parsed = json.loads(raw_json)
        return RecoveryPlan(**parsed)