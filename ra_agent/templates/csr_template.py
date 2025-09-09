"""
RA Document Templates - Clinical Study Report (CSR) Template
"""

CSR_TEMPLATE = {
    "title": "Clinical Study Report Template",
    "doc_type": "Clinical Study Report (CSR)",

    "sections": [
        {
            "section_id": "1.0",
            "title": "Title Page",
            "content": """[Study Title]

Protocol Number: [Protocol Number]
Sponsor: [Sponsor Name]
Investigator(s): [Principal Investigator]
Date of Report: [Report Date]

CONFIDENTIAL - Regulatory Affairs Document
"""
        },
        {
            "section_id": "2.0",
            "title": "Synopsis",
            "content": """2.1 Study Title: [Study Title]
2.2 Protocol Number: [Protocol Number]
2.3 Study Design: [Study Design - Phase, Randomized, etc.]
2.4 Objectives: [Primary and Secondary Objectives]
2.5 Number of Patients: [Total enrolled/completed]
2.6 Primary Endpoint: [Primary Endpoint and Results]
2.7 Conclusions: [Brief Conclusion]
2.8 Date of First Patient First Visit: [Date]
2.9 Date of Last Patient Last Visit: [Date]
"""
        },
        {
            "section_id": "3.0",
            "title": "Introduction",
            "content": """3.1 Study Rationale: [Scientific rationale]
3.2 Study Objectives: [Complete objectives]
3.3 Overall Study Design: [Detailed study design]
"""
        },
        {
            "section_id": "4.0",
            "title": "Study Patients",
            "content": """4.1 Inclusion Criteria:
[List inclusion criteria]

4.2 Exclusion Criteria:
[List exclusion criteria]

4.3 Demographics: [Patient demographics table]
"""
        },
        {
            "section_id": "5.0",
            "title": "Efficacy Results",
            "content": """5.1 Primary Efficacy Endpoint: [Results]
5.2 Secondary Efficacy Endpoints: [Results]
5.3 Statistical Analysis: [Methods and results]
5.4 Subgroup Analyses: [If applicable]
"""
        },
        {
            "section_id": "6.0",
            "title": "Safety Results",
            "content": """6.1 Adverse Events Summary: [AE Summary]
6.2 Serious Adverse Events: [SAE Details]
6.3 Laboratory Abnormalities: [Lab results]
6.4 Vital Signs: [Vital signs data]
"""
        },
        {
            "section_id": "7.0",
            "title": "Conclusions",
            "content": """[Overall study conclusions and recommendations]
"""
        },
        {
            "section_id": "8.0",
            "title": "References",
            "content": """[Study protocol, amendments, statistical analysis plan, etc.]
"""
        }
    ],

    "required_fields": [
        "study_title", "protocol_number", "sponsor_name",
        "principal_investigator", "report_date", "study_design",
        "objectives", "patient_count", "primary_endpoint",
        "safety_summary", "efficacy_summary"
    ],

    "target_authorities": ["FDA", "EMA", "ICH"]
}

def get_csr_template():
    """Get Clinical Study Report template"""
    return CSR_TEMPLATE

def validate_csr_data(data: dict) -> list:
    """Validate CSR data against template requirements"""
    missing_fields = []
    for field in CSR_TEMPLATE["required_fields"]:
        if field not in data or not data[field]:
            missing_fields.append(field)

    return missing_fields

def populate_csr_template(data: dict) -> str:
    """Populate CSR template with provided data"""
    content = ""

    for section in CSR_TEMPLATE["sections"]:
        section_content = section["content"]

        # Replace placeholders with data
        for key, value in data.items():
            placeholder = f"[{key.replace('_', ' ').title()}]"
            section_content = section_content.replace(placeholder, str(value))

        content += f"{section['section_id']} {section['title']}\n{section_content}\n\n"

    return content
