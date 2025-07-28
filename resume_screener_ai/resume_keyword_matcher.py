import pandas as pd


def match_keywords(df, skills_required):
    matched_skills = []

    for text in df["cleaned_text"]:
        matched = [skill for skill in skills_required if skill.lower()
                   in text.lower()]
        matched_skills.append(", ".join(matched))

    df["matched_skills"] = matched_skills
    return df


# Optional test
if __name__ == "__main__":
    test_df = pd.DataFrame({
        "cleaned_text": ["i am a python developer", "react and ml expert"]
    })
    skills = ["python", "ml", "react"]
    print(match_keywords(test_df, skills))
