import json
from pipeline import MedicalOrchestrator

def display_report(report):
    print("\n" + "=" * 65)
    print(" MEDIC-AI MULTI-AGENT DIAGNOSTIC REPORT")
    print("=" * 65)
    
    print(f"\n[PATIENT QUERY]:\n{report.patient_query}")
    
    print(f"\n--- 1. CLINICAL ASSESSMENT ---")
    print(f"• Condition: {report.assessment.primary_condition}")
    print(f"• Severity:  {report.assessment.severity}")
    print("• Observations:")
    for obs in report.assessment.key_observations:
        print(f"  - {obs}")

    print(f"\n--- 2. CARE & RECOVERY PLAN ---")
    print("• Home Remedies:")
    for rem in report.recovery.home_remedies:
        print(f"  - {rem}")
    print("• Lifestyle Tips:")
    for tip in report.recovery.lifestyle_tips:
        print(f"  - {tip}")

    print(f"\n--- 3. OTC MEDICATION & SAFETY ---")
    print("• Suggested OTC Meds:")
    for drug in report.medication.otc_drugs:
        print(f"  - {drug}")
    print(f"• Usage Guidance: {report.medication.dosage_notes}")
    print("• Precautions:")
    for w in report.medication.warnings:
        print(f"  - {w}")

    print("\n" + "=" * 65)
    print(" DISCLAIMER: Educational AI prototype. Consult a doctor for actual medical advice.")
    print("=" * 65 + "\n")

def save_report_to_disk(report):
    os.makedirs("outputs", exist_ok=True)
    filename = "outputs/latest_medical_report.json"
    
    with open(filename, "w") as f:
        f.write(report.model_dump_json(indent=2))
        
    print(f" Structured audit report saved to: {filename}")

def select_sample_case():
    try:
        with open("sample_cases.json", "r") as f:
            samples = json.load(f)
            
        print("\n SELECT A TEST CASE:")
        for idx, case in enumerate(samples, start=1):
            print(f"  [{idx}] {case.get('title', f'Case {idx}')}")
            
        choice = input("\nEnter case number (1-{}): ".format(len(samples))).strip()
        
        if choice.isdigit() and 1 <= int(choice) <= len(samples):
            selected = samples[int(choice) - 1]
            print(f"\nSelected Case #{selected['id']}: \"{selected['description']}\"")
            return selected["description"]
        else:
            print("Invalid selection. Loading default Case #1.")
            return samples[0]["description"]
            
    except FileNotFoundError:
        print("Error: 'sample_cases.json' not found.")
        return None

if __name__ == "__main__":
    orchestrator = MedicalOrchestrator()
    
    print("MEDIC-AI System Initialized.")
    print("Type your symptoms below (or type 'sample' to choose a test case):")
    
    user_input = input("\nSymptoms: ").strip()
    
    if user_input.lower() == "sample":
        user_input = select_sample_case()

    if user_input:
        report = orchestrator.process_case(user_input)
        display_report(report)