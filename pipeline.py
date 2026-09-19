import time
from agents.assessor import AssessorAgent
from agents.remedies import RemediesAgent
from agents.pharma import PharmaAgent
from schema import CompleteMedicalReport

class MedicalOrchestrator:
    def __init__(self):
        self.assessor = AssessorAgent()
        self.remedy_expert = RemediesAgent()
        self.pharma_expert = PharmaAgent()

    def process_case(self, user_symptoms: str) -> CompleteMedicalReport:
        start_total = time.time()

        print("\n [Agent 1/3] Assessor Running...")
        t0 = time.time()
        assessment = self.assessor.evaluate(user_symptoms)
        print(f"   └─ Completed in {round(time.time() - t0, 2)}s")

        print(" [Agent 2/3] Remedy Advisor Running...")
        t0 = time.time()
        remedies = self.remedy_expert.suggest_care(assessment)
        print(f"   └─ Completed in {round(time.time() - t0, 2)}s")

        print(" [Agent 3/3] Pharma Specialist Running...")
        t0 = time.time()
        meds = self.pharma_expert.recommend_meds(assessment)
        print(f"   └─ Completed in {round(time.time() - t0, 2)}s")

        print(f"\n Total Pipeline Execution: {round(time.time() - start_total, 2)}s")

        return CompleteMedicalReport(
            patient_query=user_symptoms,
            assessment=assessment,
            recovery=remedies,
            medication=meds
        )