from merger.merge_engine import MergeEngine
from models.factory import create_candidate


def test_merge():

    csv = create_candidate(
        source="CSV",
        full_name="John Smith",
        email="john@gmail.com",
        phone="9999999999",
        location="Bangalore"
    )

    resume = create_candidate(
        source="RESUME",
        full_name="John A. Smith",
        email="john@gmail.com"
    )

    merged = MergeEngine.merge(csv, resume)

    assert merged.full_name == "John A. Smith"
    assert "john@gmail.com" in merged.emails
    assert "9999999999" in merged.phones