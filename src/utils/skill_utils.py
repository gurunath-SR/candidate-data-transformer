from models.candidate import Skill


def merge_skills(skill_lists):
    """
    Remove duplicate skills while keeping the
    highest confidence value.
    """

    skill_map = {}

    for skills in skill_lists:

        for skill in skills:

            key = skill.name.strip().lower()

            if key not in skill_map:

                skill_map[key] = skill

            else:

                if skill.confidence > skill_map[key].confidence:

                    skill_map[key] = skill

    return sorted(
        skill_map.values(),
        key=lambda s: s.name
    )