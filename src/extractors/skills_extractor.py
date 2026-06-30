import re

from models.candidate import Skill
from config.skills import KNOWN_SKILLS


class SkillsExtractor:

    @staticmethod
    def extract(text: str):

        detected = []

        lower_text = text.lower()

        for skill in sorted(KNOWN_SKILLS):

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, lower_text):

                detected.append(

                    Skill(
                        name=skill.title(),
                        confidence=0.95
                    )

                )

        return detected