# import json

# from models.candidate import Candidate
# from utils.constants import SOURCE_CONFIDENCE


# class JSONParser:

#     def __init__(self, file_path):
#         self.file_path = file_path

#     def parse(self):

#         with open(self.file_path, "r", encoding="utf-8") as file:
#             data = json.load(file)

#         candidates = []

#         for item in data:

#             candidate = Candidate(
#                 full_name=item.get("full_name"),
#                 emails=[item["email"]] if item.get("email") else [],
#                 phones=[str(item["phone"])] if item.get("phone") else [],
#                 location=item.get("location"),
#                 provenance={
#                     "full_name": "JSON",
#                     "email": "JSON",
#                     "phone": "JSON",
#                     "location": "JSON"
#                 },
#                 overall_confidence=SOURCE_CONFIDENCE["JSON"]
#             )

#             candidates.append(candidate)

#         return candidates

import json

from models.factory import create_candidate


class JSONParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):

        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        candidates = []

        for item in data:

            candidate = create_candidate(
                source="JSON",
                full_name=item.get("full_name"),
                email=item.get("email"),
                phone=item.get("phone"),
                location=item.get("location"),
            )

            candidates.append(candidate)

        return candidates