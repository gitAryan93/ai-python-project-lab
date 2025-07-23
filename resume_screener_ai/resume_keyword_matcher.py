import pandas as pd


def match_keywords(csv_path, skills_required):
    df = pd.read_csv(csv_path)
    matched_skills = []
    match_score = []

    for text in df['cleaned_text']:
        skills = [skill for skill in skills_required if skill.lower()
                  in text.lower()]
        matched_skills.append(', '.join(skills))
        match_score.append(len(skills) * 10)  # 10 points per match

    df['matched_skills'] = matched_skills
    df['match_score'] = match_score

    return df
