import pandas as pd


def match_keywords(resume_text, skills):
    resume_text = resume_text.lower()
    matched = [skill for skill in skills if skill.lower() in resume_text]
    score = (len(matched) / len(skills)) * 100
    return matched, score


def process_resumes(file_path, skills):
    df = pd.read_csv(file_path)
    df['matched_skills'] = ''
    df['match_score'] = 0.0

    for index, row in df.iterrows():
        matched, score = match_keywords(row['resume'], skills)
        df.at[index, 'matched_skills'] = ', '.join(matched)
        df.at[index, 'match_score'] = round(score, 2)

    df.to_csv("filtered_resumes.csv", index=False)
    print(df[['resume', 'matched_skills', 'match_score']])


# Example usage
if __name__ == "__main__":
    skills_required = ["Python", "Machine Learning", "Pandas", "AWS", "SQL"]
    process_resumes(
        "ai-python-project-lab-backup/resume_screener_ai/resumes.csv", skills_required)
