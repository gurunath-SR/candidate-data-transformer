import re
import pdfplumber

from models.factory import create_candidate


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

        # ---------- Name ----------
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        full_name = lines[0] if lines else ""

        # ---------- Email ----------
        email_match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )

        email = email_match.group(0) if email_match else None

        # ---------- Phone ----------
        phone_match = re.search(
            r"(\+?\d[\d\s\-]{8,}\d)",
            text,
        )

        phone = phone_match.group(0) if phone_match else None

        candidate = create_candidate(
            source="RESUME",
            full_name=full_name,
            email=email,
            phone=phone,
        )

        return candidate