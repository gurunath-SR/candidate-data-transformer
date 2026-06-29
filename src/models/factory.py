from models.candidate import Candidate
from utils.constants import SOURCE_CONFIDENCE

from normalizers.name_normalizer import normalize_name
from normalizers.email_normalizer import normalize_email
from normalizers.phone_normalizer import normalize_phone
from normalizers.location_normalizer import normalize_location


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
        full_name=normalize_name(full_name),
        emails=[normalize_email(email)] if email else [],
        phones=[normalize_phone(phone)] if phone else [],
        location=normalize_location(location),
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