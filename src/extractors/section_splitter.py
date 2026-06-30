import re


class SectionSplitter:

    @staticmethod
    def split(text):

        sections = {}

        current = "header"

        sections[current] = []

        for line in text.split("\n"):

            cleaned = line.strip()

            if not cleaned:
                continue

            lower = cleaned.lower()

            if re.fullmatch(

                r"(summary|profile|skills|experience|education|projects|certifications|internships|contact)",

                lower,

            ):

                current = lower

                sections[current] = []

                continue

            sections[current].append(cleaned)

        return {

            key: "\n".join(value)

            for key, value in sections.items()

        }