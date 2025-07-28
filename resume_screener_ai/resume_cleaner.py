import os
import pandas as pd


def clean_resume_data(csv_path=None):
    # Use default path if none provided
    if csv_path is None:
        csv_path = os.path.join(os.path.dirname(__file__), 'resumes.csv')

    df = pd.read_csv(csv_path)

    # Basic Cleanup: lowercase, remove punctuation
    df['cleaned_text'] = df['resume'].str.lower(
    ).str.replace(r"[^\w\s]", '', regex=True)

    return df


# Optional: test run if you execute this file directly
if __name__ == "__main__":
    df = clean_resume_data()
    df.to_csv(os.path.join(os.path.dirname(__file__),
              "cleaned_resumes.csv"), index=False)
    print(df.head())
