from models.candidate import Candidate


class MergeEngine:

    @staticmethod
    def merge(candidate1: Candidate, candidate2: Candidate) -> Candidate:

        # Choose the candidate with higher confidence
        preferred = (
            candidate1
            if candidate1.overall_confidence >= candidate2.overall_confidence
            else candidate2
        )

        merged = Candidate(
            candidate_id=preferred.candidate_id,
            full_name=preferred.full_name,
            emails=list(set(candidate1.emails + candidate2.emails)),
            phones=list(set(candidate1.phones + candidate2.phones)),
            location=preferred.location,
            headline=preferred.headline,
            links={**candidate1.links, **candidate2.links},
            years_experience=max(
                candidate1.years_experience,
                candidate2.years_experience,
            ),
            skills=preferred.skills,
            experience=preferred.experience,
            education=preferred.education,
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