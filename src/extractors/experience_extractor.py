import re

from models.candidate import Experience


class ExperienceExtractor:

    @staticmethod
    def extract(text):

        experiences = []

        pattern = re.findall(

            r"(Machine Learning Intern|Software Engineer|Data Scientist|Backend Developer|Frontend Developer|Python Developer).*?"
            r"(Google|Microsoft|Amazon|Infosys|TCS|Wipro|Accenture|IBM).*?"
            r"(Jan.*?Present|Feb.*?Present|Mar.*?Present|\d{4}\s*-\s*\d{4})",

            text,

            re.IGNORECASE | re.DOTALL,

        )

        for role, company, duration in pattern:

            experiences.append(

                Experience(

                    company=company.strip(),

                    role=role.strip(),

                    duration=duration.strip()

                )

            )

        return experiences