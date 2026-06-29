from pathlib import Path

from parsers.csv_parser import CSVParser
from parsers.json_parser import JSONParser

BASE_DIR = Path(__file__).resolve().parent.parent

csv_file = BASE_DIR / "samples" / "candidates.csv"
json_file = BASE_DIR / "samples" / "candidates.json"

print("=" * 50)
print("CSV Candidates")
print("=" * 50)

csv_parser = CSVParser(csv_file)

for candidate in csv_parser.parse():
    print(candidate.model_dump())

print("\n" + "=" * 50)
print("JSON Candidates")
print("=" * 50)

json_parser = JSONParser(json_file)

for candidate in json_parser.parse():
    print(candidate.model_dump())
    
    
from normalizers.name_normalizer import normalize_name

print(normalize_name("john smith"))
print(normalize_name("JOHN SMITH"))
print(normalize_name("jOhN smITH"))