import pandas as pd

from models.candidate import Candidate
from utils.constants import SOURCE_CONFIDENCE

class CSVParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        df = pd.read_csv(self.file_path)

        candidates = []

        for _, row in df.iterrows():

            candidate = Candidate(
                full_name=row.get("full_name"),
                emails=[row["email"]] if pd.notna(row["email"]) else [],
                phones=[str(row["phone"])] if pd.notna(row["phone"]) else [],
                location=row.get("location"),
                provenance={
                    "full_name": "CSV",
                    "email": "CSV",
                    "phone": "CSV",
                    "location": "CSV"
                },
                overall_confidence=SOURCE_CONFIDENCE["CSV"]
            )

            candidates.append(candidate)

        return candidates