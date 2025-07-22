import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


def train_classifier(data_path, model_path, vectorizer_path):
    # Load cleaned data
    df = pd.read_csv(data_path)

    # Labels (for demo purposes, fake labels)
    df['label'] = ['ML Engineer', 'Project Manager',
                   'Frontend Developer']  # Match the sample data

    # Features
    X = df['cleaned_text']
    y = df['label']

    # Text Vectorization
    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    # Model Training
    model = LogisticRegression()
    model.fit(X_vec, y)

    # Save model and vectorizer
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)

    print("✅ Classifier trained and saved.")


# Run it
train_classifier(
    data_path='ai-python-project-lab-backup/resume_screener_ai/cleaned_resumes.csv',
    model_path='ai-python-project-lab-backup/resume_screener_ai/model.pkl',
    vectorizer_path='ai-python-project-lab-backup/resume_screener_ai/vectorizer.pkl'
)
