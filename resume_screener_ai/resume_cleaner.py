import pandas as pd


def clean_resume_data(csv_path):
    df = pd.read_csv(csv_path)

    # Basic cleanup: lowercase, remove punctuation, etc.
    df['cleaned_text'] = df['resume'].str.lower(
    ).str.replace(r'[^\w\s]', '', regex=True)

    return df


# Run it
df = clean_resume_data(
    "ai-python-project-lab-backup/resume_screener_ai/resumes.csv")

# Save cleaned CSV to disk
df.to_csv(
    "ai-python-project-lab-backup/resume_screener_ai/cleaned_resumes.csv", index=False)

print(df)
