import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def train_classifier(data_path):
    df = pd.read_csv(data_path)

    X = df['cleaned_text']
    # Assumes there's a "label" column like 'Data Scientist', 'Web Developer', etc.
    y = df['label']

    tfidf = TfidfVectorizer()
    X_tfidf = tfidf.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_tfidf, y, test_size=0.3, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    return model, tfidf


# Run it
if __name__ == "__main__":
    train_classifier(
        "ai-python-project-lab-backup/resume_screener_ai/cleaned_labeled_resumes.csv")
