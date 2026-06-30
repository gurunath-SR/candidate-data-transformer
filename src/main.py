from pathlib import Path

from logging_utils.logger import logger

from matcher.candidate_matcher import CandidateMatcher
from merger.merge_engine import MergeEngine

from parsers.csv_parser import CSVParser
from parsers.json_parser import JSONParser
from parsers.resume_parser import ResumeParser

from utils.output_writer import save_candidate


BASE_DIR = Path(__file__).resolve().parent.parent

csv_file = BASE_DIR / "samples" / "candidates.csv"
json_file = BASE_DIR / "samples" / "candidates.json"
resume_file = BASE_DIR / "samples" / "resumes" / "aryan_resume.pdf"


def main():

    try:

        logger.info("Reading CSV Candidate")
        csv_candidate = CSVParser(csv_file).parse()[0]

        logger.info("Reading JSON Candidate")
        json_candidate = JSONParser(json_file).parse()[0]

        logger.info("Reading Resume Candidate")
        resume_candidate = ResumeParser(resume_file).parse()

        logger.info("Matching Candidate")

        if CandidateMatcher.is_same_candidate(csv_candidate, resume_candidate):

            logger.info("Candidate Matched")

            merged = MergeEngine.merge(csv_candidate, resume_candidate)

            print("=" * 70)
            print("MERGED CANDIDATE")
            print("=" * 70)
            print(merged.model_dump())

            print("\n" + "=" * 70)
            print("DETECTED SKILLS")
            print("=" * 70)

            if merged.skills:
                for skill in merged.skills:
                    print("-", skill.name)
            else:
                print("No skills detected.")

            save_candidate(
                merged,
                BASE_DIR / "data" / "output" / "merged_candidate.json"
            )

            logger.info("Output Saved Successfully")

        else:

            logger.warning("Candidates do not match.")
            print("\nDifferent candidates detected.")
            print("Merge skipped.")

    except Exception as e:

        logger.exception(f"Pipeline Failed : {e}")
        print(f"\nERROR : {e}")


if __name__ == "__main__":
    main()