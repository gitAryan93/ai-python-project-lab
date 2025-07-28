# resume_cli.py

import argparse
from screener_api import process_resume
from pprint import pprint


def main():
    parser = argparse.ArgumentParser(description="Resume Screener AI CLI")
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to resume CSV file (e.g., resumes.csv)"
    )
    parser.add_argument(
        "--skills",
        type=str,
        required=True,
        help="Comma-separated skills to match (e.g., python,ml,react)"
    )

    args = parser.parse_args()
    skills = [skill.strip().lower() for skill in args.skills.split(",")]

    print(f"\n📄 Processing file: {args.input}")
    print(f"🎯 Matching skills: {skills}\n")

    result = process_resume(args.input, skills_required=skills)

    print("✅ Screener Results:")
    pprint(result)


if __name__ == "__main__":
    main()
