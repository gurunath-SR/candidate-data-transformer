from models.candidate import Candidate

from confidence.field_resolver import choose_value

from utils.skill_utils import merge_skills

from utils.profile_merge_utils import (
    merge_experience,
    merge_education,
)


class MergeEngine:

    @staticmethod
    def merge(candidate1: Candidate, candidate2: Candidate):

        merged = Candidate(

            candidate_id=choose_value(
                candidate1.candidate_id,
                candidate1.overall_confidence,
                candidate2.candidate_id,
                candidate2.overall_confidence,
            ),

            full_name=choose_value(
                candidate1.full_name,
                candidate1.overall_confidence,
                candidate2.full_name,
                candidate2.overall_confidence,
            ),

            emails=list(
                set(
                    candidate1.emails +
                    candidate2.emails
                )
            ),

            phones=list(
                set(
                    candidate1.phones +
                    candidate2.phones
                )
            ),

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

            links={
                **candidate1.links,
                **candidate2.links,
            },

            years_experience=max(
                candidate1.years_experience,
                candidate2.years_experience,
            ),

            skills=merge_skills([
                candidate1.skills,
                candidate2.skills,
            ]),

            experience=merge_experience([
                candidate1.experience,
                candidate2.experience,
            ]),

            education=merge_education([
                candidate1.education,
                candidate2.education,
            ]),

            provenance={
                **candidate1.provenance,
                **candidate2.provenance,
            },
        )

        # -----------------------------------------
        # Field Confidence Calculation
        # -----------------------------------------

        merged.field_confidence = {

            "full_name": 1 if merged.full_name else 0,

            "emails": 1 if merged.emails else 0,

            "phones": 1 if merged.phones else 0,

            "location": 1 if merged.location else 0,

            "headline": 1 if merged.headline else 0,

            "skills": 1 if merged.skills else 0,

            "experience": 1 if merged.experience else 0,

            "education": 1 if merged.education else 0,

            "links": 1 if merged.links else 0,

        }

        merged.overall_confidence = round(

            sum(merged.field_confidence.values())

            / len(merged.field_confidence),

            2,

        )

        return merged