import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def rank_resumes(csv_path, job_description):
    df = pd.read_csv(csv_path)

    # Fill NA
    df['cleaned_text'] = df['cleaned_text'].fillna('')

    # Combine resumes + job description
    all_texts = df['cleaned_text'].tolist() + [job_description]

    # TF-IDF Vectorization
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(all_texts)

    # Cosine similarity (last row is job description)
    cosine_sim = cosine_similarity(tfidf_matrix[:-1], tfidf_matrix[-1])

    # Add similarity score to DataFrame
    df['relevance_score'] = cosine_sim.flatten()

    # Rank resumes
    ranked = df.sort_values(by='relevance_score', ascending=False)

    print("🏆 Top 3 Ranked Resumes Based on Job Description:\n")
    print(ranked[['resume', 'relevance_score']].head(3))

    return ranked


# ---- RUN ----
if __name__ == "__main__":
    job_description = input("Enter job description or required skills: ")
    rank_resumes(
        "ai-python-project-lab-backup/resume_screener_ai/cleaned_resumes.csv", job_description)
