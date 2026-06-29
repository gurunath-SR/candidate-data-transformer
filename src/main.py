from models.candidate import Candidate

candidate = Candidate(
    full_name="John Smith",
    emails=["john@gmail.com"],
    phones=["9876543210"]
)

print(candidate.model_dump())