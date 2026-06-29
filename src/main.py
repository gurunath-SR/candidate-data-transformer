from pathlib import Path

from parsers.csv_parser import CSVParser
from parsers.resume_parser import ResumeParser
from merger.merge_engine import MergeEngine

BASE_DIR = Path(__file__).resolve().parent.parent

csv_file = BASE_DIR / "samples" / "candidates.csv"
resume_file = BASE_DIR / "samples" / "resumes" / "john_resume.pdf"

csv_candidate = CSVParser(csv_file).parse()[0]
resume_candidate = ResumeParser(resume_file).parse()

merged = MergeEngine.merge(csv_candidate, resume_candidate)

print("=" * 60)
print("CSV Candidate")
print("=" * 60)
print(csv_candidate.model_dump())

print("\n" + "=" * 60)
print("Resume Candidate")
print("=" * 60)
print(resume_candidate.model_dump())

print("\n" + "=" * 60)
print("Merged Candidate")
print("=" * 60)
print(merged.model_dump())