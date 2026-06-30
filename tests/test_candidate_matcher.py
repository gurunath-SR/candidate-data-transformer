from matcher.candidate_matcher import CandidateMatcher
from models.factory import create_candidate


def test_same_email():

    c1 = create_candidate(
        source="CSV",
        full_name="John Smith",
        email="john@gmail.com"
    )

    c2 = create_candidate(
        source="RESUME",
        full_name="John A Smith",
        email="john@gmail.com"
    )

    assert CandidateMatcher.is_same_candidate(c1, c2)


def test_different_candidates():

    c1 = create_candidate(
        source="CSV",
        full_name="John Smith",
        email="john@gmail.com"
    )

    c2 = create_candidate(
        source="RESUME",
        full_name="Aryan Ganesh",
        email="aryan@gmail.com"
    )

    assert not CandidateMatcher.is_same_candidate(c1, c2)