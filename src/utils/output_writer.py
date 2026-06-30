import json
from pathlib import Path


def save_candidate(candidate, output_path):

    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(output_path, "w", encoding="utf-8") as file:

        json.dump(
            candidate.model_dump(),
            file,
            indent=4,
        )

    print(f"\n✅ Output saved to:\n{output_path}")