import re
import pdfplumber

from models.factory import create_candidate
from models.candidate import Skill


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
    "html",
    "css",
    "react",
    "angular",
    "nodejs",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "git",
    "github",
    "linux",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "flask",
    "django",
}


class ResumeParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):

        text = ""

        with pdfplumber.open(self.file_path) as pdf:

            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

        lines = [line.strip() for line in text.split("\n") if line.strip()]

        full_name = lines[0] if lines else ""

        email_match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )

        email = email_match.group() if email_match else None

        phone_match = re.search(
            r"(\+?\d[\d\s\-]{8,}\d)",
            text,
        )

        phone = phone_match.group() if phone_match else None

        found_skills = []

        lower_text = text.lower()

        for skill in sorted(KNOWN_SKILLS):

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, lower_text):

                found_skills.append(

                    Skill(
                        name=skill.title(),
                        confidence=0.95,
                    )

                )

        candidate = create_candidate(
            source="RESUME",
            full_name=full_name,
            email=email,
            phone=phone,
        )

        candidate.skills = found_skills

        return candidate