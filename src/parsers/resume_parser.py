import re
import pdfplumber

from models.factory import create_candidate

from extractors.skills_extractor import SkillsExtractor
from extractors.experience_extractor import ExperienceExtractor
from extractors.education_extractor import EducationExtractor
from extractors.links_extractor import LinksExtractor
from extractors.experience_calculator import ExperienceCalculator


class ResumeParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):

        text = ""

        # -----------------------------------
        # Extract Text from PDF
        # -----------------------------------

        with pdfplumber.open(self.file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text + "\n"

        # -----------------------------------
        # Name
        # -----------------------------------

        lines = [
            line.strip()
            for line in text.split("\n")
            if line.strip()
        ]

        full_name = lines[0] if lines else ""

        # -----------------------------------
        # Email
        # -----------------------------------

        email_match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )

        email = email_match.group(0) if email_match else None

        # -----------------------------------
        # Phone
        # -----------------------------------

        phone_match = re.search(
            r"(\+?\d[\d\s\-]{8,}\d)",
            text,
        )

        phone = phone_match.group(0) if phone_match else None

        # -----------------------------------
        # Location (simple heuristic)
        # -----------------------------------

        location = None

        for line in lines:

            if any(city in line.lower() for city in [
                "bangalore",
                "bengaluru",
                "hyderabad",
                "mumbai",
                "delhi",
                "pune",
                "chennai",
                "kolkata"
            ]):

                location = line
                break

        # -----------------------------------
        # Create Candidate
        # -----------------------------------

        candidate = create_candidate(
            source="RESUME",
            full_name=full_name,
            email=email,
            phone=phone,
            location=location,
        )

        # -----------------------------------
        # Intelligent Extractors
        # -----------------------------------

        candidate.skills = SkillsExtractor.extract(text)

        candidate.experience = ExperienceExtractor.extract(text)

        candidate.education = EducationExtractor.extract(text)

        candidate.links = LinksExtractor.extract(text)

        candidate.years_experience = ExperienceCalculator.calculate(text)

        return candidate