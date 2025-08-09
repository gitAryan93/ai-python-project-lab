import argparse
import os
import json
import pandas as pd
from .screener_api import process_resume


def main():
    parser = argparse.ArgumentParser(description="Resume Screener AI CLI")
    parser.add_argument(
        "--file", "--input",
        dest="input",
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
        help="Optional: path to save results (e.g., results.json or results.csv)"
    )
    parser.add_argument(
        "--min-confidence",
        type=float,
        default=40.0,
        help="Minimum confidence percent to include a prediction (default: 40.0)"
    )

    args = parser.parse_args()
    skills = [s.strip().lower() for s in args.skills.split(",") if s.strip()]

    result = process_resume(
        args.input,
        skills_required=skills,
        min_confidence=args.min_confidence
    )

    print("\n🔍 Matched Resumes:\n")
    n = len(result.get("cleaned_text", []))
    if n == 0:
        print("No results at or above the confidence threshold.")
    else:
        for i in range(n):
            cleaned = result["cleaned_text"][i]
            skills_m = result["skills_matched"][i]
            role = result["predicted_role"][i]
            conf = result["confidence"][i]
            print(f"Result #{i+1}")
            print(f"  Predicted Role : {role}  (confidence: {conf:.2f}%)")
            print(f"  Skills Matched : {skills_m if skills_m else '(none)'}")
            print(f"  Text           : {cleaned}")
            print("-" * 60)

    if args.output:
        ext = os.path.splitext(args.output)[1].lower()
        if ext == ".json":
            with open(args.output, "w") as f:
                json.dump(result, f, indent=2)
            print(f"\nSaved JSON to {args.output}")
        elif ext == ".csv":
            df = pd.DataFrame(result)
            df.to_csv(args.output, index=False)
            print(f"\nSaved CSV to {args.output}")
        else:
            print("\n⚠️ Unsupported output format. Use .json or .csv")


if __name__ == "__main__":
    main()
