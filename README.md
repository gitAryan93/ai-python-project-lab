# AI Python Project Lab

A curated collection of Python mini-projects by **Aryan Haidary**.  
Focus: core programming, algorithms, and applied ML that’s actually runnable.

---

## 🔥 Featured Project — Resume Screener AI (ML Capstone)

A command-line tool that:

- Cleans and processes resume text
- Matches resumes against required skills
- Predicts job roles with a trained ML model
- Exports results with confidence scores

### Quickstart

````bash
# From repo root
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run tests
python -m unittest -v resume_screener_ai.test_screener

# Run screener
python -m resume_screener_ai.resume_cli \
  --file resume_screener_ai/resumes.csv \
  --skills "python, ml, react" \
  --min-confidence 40 \
  --output results.csv

 **Arguments:**
- `--file` / `--input`: Path to resume CSV file (e.g., `resumes.csv`)
- `--skills`: Comma-separated skills to match (e.g., `python,ml,react`)
- `--output`: Optional — path to save results (`.json` or `.csv`)
- `--min-confidence`: Minimum confidence percentage for predictions (default: `40.0`)

---

### 📌 Example Output
```bash
🔍 Matched Resumes:

Result #1
  Predicted Role : Web Developer  (confidence: 45.58%)
  Skills Matched : python, ml
  Text           : i am a software engineer with python and ml experience
------------------------------------------------------------

Saved CSV to results.csv

## 🛠 Troubleshooting

If you see:
````

ModuleNotFoundError: No module named 'resume_screener_ai'

````
Run the following from your repo root:
```bash
source venv/bin/activate
pip install -r requirements.txt
````

This will activate your virtual environment and install all required packages.
