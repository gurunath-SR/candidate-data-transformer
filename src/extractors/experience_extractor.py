import re

from models.candidate import Experience


class ExperienceExtractor:

    @staticmethod
    def extract(text):

        experience = []

        pattern = re.findall(

            r"([A-Za-z ]+)\n([A-Za-z ]+)\n((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).+)",

            text,

            re.I

        )

        for company, role, duration in pattern:

            experience.append(

                Experience(

                    company=company.strip(),

                    role=role.strip(),

                    duration=duration.strip()

                )

            )

        return experience