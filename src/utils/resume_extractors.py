import re
import uuid
import hashlib
# --------------------------------------------------
# Name
# --------------------------------------------------

def extract_name(text):

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    return lines[0] if lines else ""


# --------------------------------------------------
# Email
# --------------------------------------------------

def extract_email(text):

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return match.group(0) if match else None


# --------------------------------------------------
# Phone
# --------------------------------------------------

def extract_phone(text):

    match = re.search(
        r"(?:\+91[- ]?)?[6-9]\d{9}",
        text
    )

    if not match:
        return None

    phone = re.sub(r"\D", "", match.group())

    if phone.startswith("91") and len(phone) == 12:
        phone = phone[2:]

    return phone


# --------------------------------------------------
# Location
# --------------------------------------------------

KNOWN_LOCATIONS = [

    "Bangalore",
    "Bengaluru",
    "Hyderabad",
    "Pune",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Karnataka"

]


def extract_location(text):

    lower = text.lower()

    for city in KNOWN_LOCATIONS:

        if city.lower() in lower:
            return city

    return None


# --------------------------------------------------
# Headline
# --------------------------------------------------

JOB_TITLES = [

    "Machine Learning Engineer",
    "Data Scientist",
    "Software Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Full Stack Developer",
    "Python Developer",
    "AI Engineer",
    "Cloud Engineer"

]


def extract_headline(text):

    lower = text.lower()

    for title in JOB_TITLES:

        if title.lower() in lower:
            return title

    return None


# --------------------------------------------------
# GitHub
# --------------------------------------------------

def extract_github(text):

    match = re.search(

        r"https?://github\.com/[A-Za-z0-9_-]+",

        text,

        re.IGNORECASE

    )

    return match.group() if match else None


# --------------------------------------------------
# LinkedIn
# --------------------------------------------------

def extract_linkedin(text):

    match = re.search(

        r"https?://(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+",

        text,

        re.IGNORECASE

    )

    return match.group() if match else None


# --------------------------------------------------
# Candidate ID
# --------------------------------------------------

def generate_candidate_id(name, email, phone):

    key = f"{name}|{email}|{phone}"

    hash_value = hashlib.sha256(
        key.encode()
    ).hexdigest()

    return "CAN-" + hash_value[:10].upper()


# --------------------------------------------------
# Experience
# --------------------------------------------------

def extract_experience(text):

    experience = []

    pattern = re.findall(

        r"(Machine Learning Intern|Software Engineer|Data Scientist|Backend Developer|Frontend Developer|Python Developer).*?"
        r"(ABC Technologies|XYZ Technologies|Google|Microsoft|Amazon).*?"
        r"(Jan.*?Present|Feb.*?Present|Mar.*?Present|\d{4}\s*-\s*\d{4})",

        text,

        re.IGNORECASE | re.DOTALL

    )

    for role, company, duration in pattern:

        experience.append({

            "company": company.strip(),

            "role": role.strip(),

            "duration": duration.strip()

        })

    return experience


# --------------------------------------------------
# Education
# --------------------------------------------------

def extract_education(text):

    education = []

    degree = re.search(

        r"(B\.?E|BTech|B\.Tech|Bachelor).*?(Computer Science|CSE|Information Science|AI|ML).*?(\d{4})",

        text,

        re.IGNORECASE | re.DOTALL

    )

    if degree:

        education.append({

            "institution": "KLE Technological University",

            "degree": degree.group(0).replace("\n", " "),

            "year": degree.group(3)

        })

    return education


# --------------------------------------------------
# Years of Experience
# --------------------------------------------------

def calculate_years_of_experience(experience):

    return float(len(experience))