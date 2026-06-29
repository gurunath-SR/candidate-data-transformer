from models.candidate import Candidate
from confidence.field_resolver import choose_value


class MergeEngine:

    @staticmethod
    def merge(candidate1: Candidate, candidate2: Candidate):

        merged = Candidate(

            full_name=choose_value(
                candidate1.full_name,
                candidate1.overall_confidence,
                candidate2.full_name,
                candidate2.overall_confidence,
            ),

            emails=list(set(candidate1.emails + candidate2.emails)),

            phones=list(set(candidate1.phones + candidate2.phones)),

            location=choose_value(
                candidate1.location,
                candidate1.overall_confidence,
                candidate2.location,
                candidate2.overall_confidence,
            ),

            headline=choose_value(
                candidate1.headline,
                candidate1.overall_confidence,
                candidate2.headline,
                candidate2.overall_confidence,
            ),

            links={**candidate1.links, **candidate2.links},

            years_experience=max(
                candidate1.years_experience,
                candidate2.years_experience,
            ),

            skills=candidate1.skills + candidate2.skills,

            experience=candidate1.experience + candidate2.experience,

            education=candidate1.education + candidate2.education,

            provenance={
                **candidate1.provenance,
                **candidate2.provenance,
            },

            overall_confidence=max(
                candidate1.overall_confidence,
                candidate2.overall_confidence,
            ),
        )

        return merged