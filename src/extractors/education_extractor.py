import re

from models.candidate import Education


class EducationExtractor:

    @staticmethod
    def extract(text):

        education = []

        degree = re.search(

            r"(B\.?E|BTech|B\.Tech|Bachelor).*?"
            r"(Computer Science|CSE|Information Science|AI|ML).*?"
            r"(\d{4})",

            text,

            re.IGNORECASE | re.DOTALL,

        )

        if degree:

            education.append(

                Education(

                    institution="Unknown",

                    degree=degree.group().replace("\n", " "),

                    year=degree.group(3)

                )

            )

        return education