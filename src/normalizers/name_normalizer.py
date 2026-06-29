def normalize_name(name: str) -> str:
    """
    Normalize a person's name.

    Example:
        john smith
        JOHN SMITH
        jOhN SmItH

    becomes

        John Smith
    """

    if not name:
        return ""

    name = name.strip()

    return " ".join(word.capitalize() for word in name.split())