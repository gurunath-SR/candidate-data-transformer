import re

from models.candidate import Education
from config.degrees import KNOWN_DEGREES


class EducationExtractor:

    @staticmethod
    def extract(text):

        education = []

        year_match = re.search(r"(20\d{2})", text)

        year = year_match.group(1) if year_match else None

        for degree in KNOWN_DEGREES:

            if degree.lower() in text.lower():

                education.append(

                    Education(
                        institution="Unknown",
                        degree=degree,
                        year=year
                    )

                )

                break

        return education