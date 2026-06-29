from models.candidate import Candidate
from utils.constants import SOURCE_CONFIDENCE


def create_candidate(
    source,
    full_name=None,
    email=None,
    phone=None,
    location=None,
    headline=None,
    links=None,
):
    return Candidate(
        full_name=full_name,
        emails=[email] if email else [],
        phones=[str(phone)] if phone else [],
        location=location,
        headline=headline,
        links=links or {},
        provenance={
            "full_name": source,
            "email": source,
            "phone": source,
            "location": source,
        },
        overall_confidence=SOURCE_CONFIDENCE[source],
    )