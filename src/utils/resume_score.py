def calculate_resume_score(candidate):

    fields = {
        "Name": bool(candidate.full_name),
        "Email": len(candidate.emails) > 0,
        "Phone": len(candidate.phones) > 0,
        "Location": bool(candidate.location),
        "Headline": bool(candidate.headline),
        "Skills": len(candidate.skills) > 0,
        "Experience": len(candidate.experience) > 0,
        "Education": len(candidate.education) > 0,
        "GitHub": "github" in candidate.links,
        "LinkedIn": "linkedin" in candidate.links,
    }

    score = sum(fields.values())

    percentage = round(score / len(fields) * 100)

    return percentage, fields