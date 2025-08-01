# run_screener.py

from screener_api import process_resume
from pprint import pprint

# Example: Single CSV with multiple resumes
file_path = "resume_screener_ai/resumes.csv"
skills_required = ["python", "ml", "react"]

result = process_resume(file_path, skills_required)
pprint(result)
