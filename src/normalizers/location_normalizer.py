def normalize_location(location: str) -> str:

    if not location:
        return ""

    return location.strip().title()