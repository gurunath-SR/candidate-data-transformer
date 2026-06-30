import re
from datetime import datetime


class ExperienceCalculator:

    @staticmethod
    def calculate(text):

        current_year = datetime.now().year

        years = re.findall(r"(20\d{2})", text)

        if not years:
            return 0.0

        earliest = min(map(int, years))

        return round(current_year - earliest, 1)