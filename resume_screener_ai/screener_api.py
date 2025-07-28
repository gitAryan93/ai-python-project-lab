# screener_api.py

import os
import pandas as pd
import joblib
from resume_cleaner import clean_resume_data
from resume_keyword_matcher import match_keywords

# Load model + vectorizer
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def process_resume(file_path, skills_required):
    # 1. Clean resume
    df = pd.read_csv(file_path) if file_path.endswith(
        ".csv") else pd.DataFrame({"resume": [open(file_path).read()]})
    df_cleaned = clean_resume_data(file_path)

    # 2. Match skills
    df_skills = match_keywords(df_cleaned, skills_required)

    # 3. Vectorize cleaned text
    X = vectorizer.transform(df_cleaned["cleaned_text"])

    # 4. Predict role
    predictions = model.predict(X)
    probabilities = model.predict_proba(X)

    # 5. Return results
    return {
        "cleaned_text": df_cleaned["cleaned_text"].tolist(),
        "skills_matched": df_skills["matched_skills"].tolist(),
        "predicted_role": predictions.tolist(),
        "confidence": [round(max(p) * 100, 2) for p in probabilities]
    }


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "resumes.csv")
    result = process_resume(file_path, skills_required=[
                            "python", "ml", "react"])
    from pprint import pprint
    pprint(result)
