def calculate_candidate_rank(candidate):

    score = 0

    # -------------------------
    # Skills
    # -------------------------
    score += len(candidate.skills) * 3

    # -------------------------
    # Experience
    # -------------------------
    score += candidate.years_experience * 10

    # -------------------------
    # Education
    # -------------------------
    score += len(candidate.education) * 10

    # -------------------------
    # Headline
    # -------------------------
    if candidate.headline:
        score += 5

    # -------------------------
    # GitHub
    # -------------------------
    if "github" in candidate.links:
        score += 5

    # -------------------------
    # LinkedIn
    # -------------------------
    if "linkedin" in candidate.links:
        score += 5

    # -------------------------
    # Resume Completeness
    # -------------------------
    score += candidate.overall_confidence * 20

    return round(score, 2)