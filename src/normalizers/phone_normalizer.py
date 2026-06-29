import re


def normalize_phone(phone: str) -> str:

    if not phone:
        return ""

    digits = re.sub(r"\D", "", str(phone))

    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]

    return digits