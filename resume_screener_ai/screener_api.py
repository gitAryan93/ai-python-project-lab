import os
import pandas as pd
import joblib
from .resume_cleaner import clean_resume_data
from .resume_keyword_matcher import match_keywords

# Load model and vectorizer
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def process_resume(file_path, skills_required, min_confidence=40.0):
    """
    Process resumes: clean text, match skills, predict role, and return filtered results.
    Args:
        file_path (str): Path to resume CSV file.
        skills_required (list): List of skills to match.
        min_confidence (float): Minimum confidence % required to keep a prediction.
    Returns:
        dict: Filtered results containing cleaned_text, skills_matched, predicted_role, confidence.
    """

    # Step 1: Load and clean resumes
    df = pd.read_csv(file_path) if file_path.endswith(".csv") else pd.DataFrame({
        "resume": [open(file_path).read()]
    })
    df_cleaned = clean_resume_data(file_path)

    # Step 2: Match keywords
    df_skills = match_keywords(df_cleaned, skills_required)

    # Step 3: Vectorize resumes
    X = vectorizer.transform(df_cleaned["cleaned_text"])

    # Step 4: Predict role + probability
    predictions = model.predict(X)
    probabilities = model.predict_proba(X)
    confidence = [float(round(max(p) * 100, 2)) for p in probabilities]

    # Step 5: Filter low-confidence results
    filtered_results = {
        "cleaned_text": [],
        "skills_matched": [],
        "predicted_role": [],
        "confidence": [],
    }

    for i in range(len(confidence)):
        if confidence[i] >= min_confidence:
            filtered_results["cleaned_text"].append(
                df_skills.loc[i, "cleaned_text"])
            filtered_results["skills_matched"].append(
                df_skills.loc[i, "matched_skills"])
            filtered_results["predicted_role"].append(predictions[i])
            filtered_results["confidence"].append(confidence[i])

    return filtered_results


# Optional test run
if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "resumes.csv")
    result = process_resume(file_path, skills_required=[
                            "python", "ml", "react"])
    from pprint import pprint
    pprint(result)
