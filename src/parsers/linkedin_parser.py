import json

from models.factory import create_candidate
from models.candidate import Skill, Experience, Education


class LinkedInParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        candidate = create_candidate(

            source="JSON",

            full_name=data.get("full_name"),

            email=data.get("email"),

            phone=data.get("phone"),

            location=data.get("location"),

            headline=data.get("headline"),

            links={
                "github": data.get("github", ""),
                "linkedin": data.get("linkedin", "")
            }

        )

        candidate.skills = [

            Skill(
                name=skill,
                confidence=0.98
            )

            for skill in data.get("skills", [])

        ]

        candidate.experience = [

            Experience(

                company=item["company"],

                role=item["role"],

                duration=item["duration"]

            )

            for item in data.get("experience", [])

        ]

        candidate.education = [

            Education(

                institution=item["institution"],

                degree=item["degree"],

                year=item["year"]

            )

            for item in data.get("education", [])

        ]

        return candidate