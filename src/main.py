"""
Candidate Data Transformer

Version : 2.0

Author : Gurunath Rachannavar

Description:
Multi-source Candidate Parsing, Matching,
Normalization and Intelligent Profile Merging.
"""


from pathlib import Path

from logging_utils.logger import logger

from matcher.candidate_matcher import CandidateMatcher
from merger.merge_engine import MergeEngine

from parsers.csv_parser import CSVParser
from parsers.json_parser import JSONParser
from parsers.resume_parser import ResumeParser

from utils.output_writer import save_candidate
from parsers.linkedin_parser import LinkedInParser
from utils.resume_score import calculate_resume_score
from utils.candidate_ranker import calculate_candidate_rank
from utils.candidate_summary import print_candidate_summary


BASE_DIR = Path(__file__).resolve().parent.parent

csv_file = BASE_DIR / "samples" / "candidates.csv"
json_file = BASE_DIR / "samples" / "candidates.json"
resume_file = BASE_DIR / "samples" / "resumes" / "aryan_resume.pdf"
linkedin_file = BASE_DIR / "samples" / "linkedin_profile.json"


def main():

    try:

        logger.info("Reading CSV Candidate")
        csv_candidate = CSVParser(csv_file).parse()[0]

        logger.info("Reading JSON Candidate")
        json_candidate = JSONParser(json_file).parse()[0]

        logger.info("Reading Resume Candidate")
        resume_candidate = ResumeParser(resume_file).parse()

        logger.info("Reading linkdin Candidate")
        linkedin_candidate = LinkedInParser(linkedin_file).parse()
        
        logger.info("Matching Candidate")

        if CandidateMatcher.is_same_candidate(csv_candidate, resume_candidate):

            logger.info("Candidate Matched")

            merged = MergeEngine.merge(csv_candidate, resume_candidate)

            print("=" * 70)
            print("MERGED CANDIDATE")
            print("=" * 70)
            print_candidate_summary(merged)

            print("\n" + "=" * 70)
            print("DETECTED SKILLS")
            print("=" * 70)

            print("\n" + "=" * 70)
            print("RESUME QUALITY")
            print("=" * 70)

            score, fields = calculate_resume_score(merged)

            print(f"\nOverall Resume Score : {score}%")

            stars = "★" * (score // 20) + "☆" * (5 - score // 20)

            print(stars)

            print("\nSection Status")

            for field, present in fields.items():

                symbol = "✔" if present else "✘"

                print(f"{symbol} {field}")
            
            
            print("\n" + "=" * 70)
            print("CANDIDATE RANK")
            print("=" * 70)

            rank = calculate_candidate_rank(merged)

            print(f"\nCandidate Score : {rank}")

            if rank >= 90:
                print("★★★★★ Outstanding Candidate")

            elif rank >= 70:
                print("★★★★☆ Strong Candidate")

            elif rank >= 50:
                print("★★★☆☆ Good Candidate")

            elif rank >= 30:
                print("★★☆☆☆ Average Candidate")

            else:
                print("★☆☆☆☆ Needs Improvement")
            
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