from pathlib import Path

from parsers.csv_parser import CSVParser
from parsers.json_parser import JSONParser
from merger.merge_engine import MergeEngine

BASE_DIR = Path(__file__).resolve().parent.parent

csv_file = BASE_DIR / "samples" / "candidates.csv"
json_file = BASE_DIR / "samples" / "candidates.json"

csv_candidates = CSVParser(csv_file).parse()
json_candidates = JSONParser(json_file).parse()

print("=" * 60)
print("MERGED CANDIDATE")
print("=" * 60)

merged = MergeEngine.merge(csv_candidates[0], json_candidates[0])

print(merged.model_dump())