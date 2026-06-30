import re


class ContactExtractor:

    @staticmethod
    def extract_name(text):

        lines = [
            line.strip()
            for line in text.split("\n")
            if line.strip()
        ]

        return lines[0] if lines else ""

    @staticmethod
    def extract_email(text):

        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )

        return match.group() if match else None

    @staticmethod
    def extract_phone(text):

        match = re.search(
            r"(?:\+91[- ]?)?[6-9]\d{9}",
            text,
        )

        if not match:
            return None

        phone = re.sub(r"\D", "", match.group())

        if phone.startswith("91") and len(phone) == 12:
            phone = phone[2:]

        return phone

    @staticmethod
    def extract_location(text):

        cities = [

            "Bangalore",
            "Bengaluru",
            "Hyderabad",
            "Pune",
            "Mumbai",
            "Delhi",
            "Chennai",
            "Kolkata",
            "Noida",
            "Gurgaon"

        ]

        lower = text.lower()

        for city in cities:

            if city.lower() in lower:

                return city

        return None

    @staticmethod
    def extract_github(text):

        match = re.search(

            r"https?://github\.com/[A-Za-z0-9_-]+",

            text,

            re.IGNORECASE,

        )

        return match.group() if match else None

    @staticmethod
    def extract_linkedin(text):

        match = re.search(

            r"https?://(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+",

            text,

            re.IGNORECASE,

        )

        return match.group() if match else None

    @staticmethod
    def extract_headline(text):

        titles = [

            "Machine Learning Engineer",
            "Data Scientist",
            "Software Engineer",
            "Backend Developer",
            "Frontend Developer",
            "Full Stack Developer",
            "Python Developer",
            "AI Engineer",
            "Cloud Engineer"

        ]

        lower = text.lower()

        for title in titles:

            if title.lower() in lower:

                return title

        return None