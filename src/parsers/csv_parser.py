# import pandas as pd

# from models.factory import create_candidate
# from utils.constants import SOURCE_CONFIDENCE

# class CSVParser:

#     def __init__(self, file_path):
#         self.file_path = file_path

#     def parse(self):
#         df = pd.read_csv(self.file_path)

#         candidates = []

#         for _, row in df.iterrows():

#             candidate = Candidate(
#                 full_name=row.get("full_name"),
#                 emails=[row["email"]] if pd.notna(row["email"]) else [],
#                 phones=[str(row["phone"])] if pd.notna(row["phone"]) else [],
#                 location=row.get("location"),
#                 provenance={
#                     "full_name": "CSV",
#                     "email": "CSV",
#                     "phone": "CSV",
#                     "location": "CSV"
#                 },
#                 overall_confidence=SOURCE_CONFIDENCE["CSV"]
#             )

#             candidates.append(candidate)

#         return candidates


import pandas as pd

from models.factory import create_candidate


class CSVParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):

        df = pd.read_csv(self.file_path)

        candidates = []

        for _, row in df.iterrows():

            candidate = create_candidate(
                source="CSV",
                full_name=row.get("full_name"),
                email=row.get("email"),
                phone=row.get("phone"),
                location=row.get("location"),
            )

            candidates.append(candidate)

        return candidates