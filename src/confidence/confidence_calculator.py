from models.candidate import Candidate


class ConfidenceCalculator:

    @staticmethod
    def calculate(candidate: Candidate):

        scores = {}

        scores["full_name"] = 1 if candidate.full_name else 0

        scores["emails"] = 1 if candidate.emails else 0

        scores["phones"] = 1 if candidate.phones else 0

        scores["location"] = 1 if candidate.location else 0

        scores["headline"] = 1 if candidate.headline else 0

        scores["skills"] = 1 if candidate.skills else 0

        scores["experience"] = 1 if candidate.experience else 0

        scores["education"] = 1 if candidate.education else 0

        scores["links"] = 1 if candidate.links else 0

        overall = round(
            sum(scores.values()) / len(scores),
            2
        )

        return scores, overall