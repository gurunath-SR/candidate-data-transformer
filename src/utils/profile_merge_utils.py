from models.candidate import Experience, Education


def merge_experience(exp_lists):
    """
    Merge duplicate experience entries.
    """

    merged = {}

    for experiences in exp_lists:

        for exp in experiences:

            key = (
                exp.company.strip().lower(),
                exp.role.strip().lower()
            )

            if key not in merged:
                merged[key] = exp

    return list(merged.values())


def merge_education(edu_lists):
    """
    Merge duplicate education entries.
    """

    merged = {}

    for educations in edu_lists:

        for edu in educations:

            key = (
                edu.institution.strip().lower(),
                edu.degree.strip().lower()
            )

            if key not in merged:
                merged[key] = edu

    return list(merged.values())