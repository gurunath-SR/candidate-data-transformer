def print_candidate_summary(candidate):

    print("\n" + "=" * 70)
    print("RECRUITER SUMMARY")
    print("=" * 70)

    print(f"Candidate ID        : {candidate.candidate_id}")
    print(f"Name                : {candidate.full_name}")

    print(
        f"Email               : {', '.join(candidate.emails) if candidate.emails else 'N/A'}"
    )

    print(
        f"Phone               : {', '.join(candidate.phones) if candidate.phones else 'N/A'}"
    )

    print(f"Location            : {candidate.location or 'N/A'}")

    print(f"Headline            : {candidate.headline or 'N/A'}")

    print(f"Years Experience    : {candidate.years_experience}")

    print()

    print("Skills")

    if candidate.skills:

        for skill in candidate.skills:
            print(f"  • {skill.name}")

    else:

        print("  None")

    print()

    print("Experience")

    if candidate.experience:

        for exp in candidate.experience:

            print(
                f"  • {exp.role} | {exp.company} | {exp.duration}"
            )

    else:

        print("  None")

    print()

    print("Education")

    if candidate.education:

        for edu in candidate.education:

            print(
                f"  • {edu.degree}"
            )

            print(
                f"    {edu.institution}"
            )

            print(
                f"    {edu.year}"
            )

    else:

        print("  None")

    print()

    print("Links")

    if candidate.links:

        for key, value in candidate.links.items():

            print(f"  {key.title()} : {value}")

    else:

        print("  None")

    print()

    print(f"Overall Confidence : {candidate.overall_confidence}")