import pdfplumber

from models.factory import create_candidate
from models.candidate import Skill, Experience, Education

from utils.resume_extractors import (
    extract_name,
    extract_email,
    extract_phone,
    extract_location,
    extract_headline,
    extract_github,
    extract_linkedin,
    extract_experience,
    extract_education,
    calculate_years_of_experience,
    generate_candidate_id,
)

# -------------------------------------------------
# Known Skills
# -------------------------------------------------

KNOWN_SKILLS = {
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "react",
    "nodejs",
    "express",
    "docker",
    "kubernetes",
    "aws",
    "git",
    "github",
    "linux",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "tensorflow",
    "keras",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "flask",
    "django"
}


class ResumeParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):

        # ---------------------------------------
        # Read Resume
        # ---------------------------------------

        text = ""

        with pdfplumber.open(self.file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        # ---------------------------------------
        # Extract Basic Information
        # ---------------------------------------

        full_name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone(text)
        location = extract_location(text)
        headline = extract_headline(text)

        github = extract_github(text)
        linkedin = extract_linkedin(text)

        # ---------------------------------------
        # Links Dictionary
        # ---------------------------------------

        links = {}

        if github:
            links["github"] = github

        if linkedin:
            links["linkedin"] = linkedin

        # ---------------------------------------
        # Create Candidate
        # ---------------------------------------

        candidate = create_candidate(
            source="RESUME",
            full_name=full_name,
            email=email,
            phone=phone,
            location=location,
            headline=headline,
            links=links
        )

        # ---------------------------------------
        # Candidate ID
        # ---------------------------------------

        candidate.candidate_id = generate_candidate_id(

        candidate.full_name,

        candidate.emails[0] if candidate.emails else "",

        candidate.phones[0] if candidate.phones else ""

        )

        # ---------------------------------------
        # Skills
        # ---------------------------------------

        lower_text = text.lower()

        skills = []

        for skill in sorted(KNOWN_SKILLS):

            if skill.lower() in lower_text:

                skills.append(
                    Skill(
                        name=skill.title(),
                        confidence=0.95
                    )
                )

        candidate.skills = skills

        # ---------------------------------------
        # Experience
        # ---------------------------------------

        extracted_experience = extract_experience(text)

        candidate.experience = [
            Experience(
                company=item["company"],
                role=item["role"],
                duration=item["duration"]
            )
            for item in extracted_experience
        ]

        # ---------------------------------------
        # Education
        # ---------------------------------------

        extracted_education = extract_education(text)

        candidate.education = [
            Education(
                institution=item["institution"],
                degree=item["degree"],
                year=item["year"]
            )
            for item in extracted_education
        ]

        # ---------------------------------------
        # Years of Experience
        # ---------------------------------------

        candidate.years_experience = calculate_years_of_experience(
            extracted_experience
        )

        return candidate