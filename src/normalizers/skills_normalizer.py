def normalize_skills(skills):

    normalized = []

    for skill in skills:

        skill = skill.strip().title()

        if skill not in normalized:
            normalized.append(skill)

    return normalized