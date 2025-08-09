import os
import pandas as pd
from .resume_cleaner import clean_resume_data
from .resume_keyword_matcher import match_keywords
from .resume_classifier_ai import train_classifier

# Get the current directory of the script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    print("🧼 Cleaning resumes...")
    df_cleaned = clean_resume_data(os.path.join(CURRENT_DIR, "resumes.csv"))
    df_cleaned.to_csv(os.path.join(
        CURRENT_DIR, "cleaned_resumes.csv"), index=False)

    print("🔍 Matching skills...")
    skills_required = [
        "Python", "Django", "SQL", "Excel",
        "Project", "Leadership", "React", "REST", "Machine Learning"
    ]
    df_with_skills = match_keywords(
        os.path.join(CURRENT_DIR, "cleaned_resumes.csv"),
        skills_required
    )
    df_with_skills.to_csv(os.path.join(
        CURRENT_DIR, "resume_with_skills.csv"), index=False)

    print("🧠 Classifying roles...")
    train_classifier(
        os.path.join(CURRENT_DIR, "cleaned_labeled_resumes.csv"),
        os.path.join(CURRENT_DIR, "model.pkl"),
        os.path.join(CURRENT_DIR, "vectorizer.pkl")
    )

    print("✅ Done! Classifier trained and saved.")


if __name__ == "__main__":
    main()
