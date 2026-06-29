# from parsers.csv_parser import CSVParser


# parser = CSVParser("samples/candidates.csv")

# candidates = parser.parse()

# for candidate in candidates:
#     print(candidate.model_dump())

from pathlib import Path
from parsers.csv_parser import CSVParser

BASE_DIR = Path(__file__).resolve().parent.parent
csv_file = BASE_DIR / "samples" / "candidates.csv"

parser = CSVParser(csv_file)

candidates = parser.parse()

for candidate in candidates:
    print(candidate.model_dump())