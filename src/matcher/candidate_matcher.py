from difflib import SequenceMatcher


class CandidateMatcher:

    @staticmethod
    def name_similarity(name1: str, name2: str) -> float:
        """
        Returns similarity between two names (0.0 - 1.0)
        """

        if not name1 or not name2:
            return 0.0

        return SequenceMatcher(
            None,
            name1.lower(),
            name2.lower()
        ).ratio()

    @staticmethod
    def is_same_candidate(candidate1, candidate2) -> bool:
        """
        Determine whether two candidate profiles belong
        to the same person.
        """

        # Rule 1 - Same Email
        if set(candidate1.emails) & set(candidate2.emails):
            return True

        # Rule 2 - Same Phone
        if set(candidate1.phones) & set(candidate2.phones):
            return True

        # Rule 3 - Similar Name
        similarity = CandidateMatcher.name_similarity(
            candidate1.full_name,
            candidate2.full_name
        )

        if similarity >= 0.90:
            return True

        return False