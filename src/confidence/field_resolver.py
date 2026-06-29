def choose_value(value1, confidence1, value2, confidence2):
    """
    Select the best value based on availability and confidence.
    """

    # Only second value exists
    if not value1 and value2:
        return value2

    # Only first value exists
    if value1 and not value2:
        return value1

    # Both missing
    if not value1 and not value2:
        return None

    # Both exist -> choose higher confidence
    if confidence2 > confidence1:
        return value2

    return value1