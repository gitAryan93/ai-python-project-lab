# resume_cli.py

import argparse
import os
import json
import pandas as pd
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
    parser.add_argument(
        "--output",
        type=str,
        help="Optional: path to save results (e.g., output.json or output.csv)"
    )

    args = parser.parse_args()
    skills = [skill.strip().lower() for skill in args.skills.split(",")]

    print(f"\n📄 Processing file: {args.input}")
    print(f"🎯 Matching skills: {skills}\n")

    result = process_resume(args.input, skills_required=skills)

    print("✅ Screener Results:")
    pprint(result)

    # Optional output saving
    if args.output:
        ext = os.path.splitext(args.output)[1].lower()

        if ext == ".json":
            with open(args.output, "w") as f:
                json.dump(result, f, indent=4)
            print(f"\n💾 Results saved to {args.output}")

        elif ext == ".csv":
            df = pd.DataFrame(result)
            df.to_csv(args.output, index=False)
            print(f"\n💾 Results saved to {args.output}")

        else:
            print("\n⚠️ Unsupported output format. Use .json or .csv")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
