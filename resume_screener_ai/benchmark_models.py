import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("cleaned_labeled_resumes.csv")
X_text = df["cleaned_text"]
y = df["label"]

# Split
X_train_text = X_test_text = X_text
y_train = y_test = y

# Vectorizers
vectorizers = {
    "CountVectorizer": CountVectorizer(),
    "TFIDF": TfidfVectorizer()
}

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(),
    "SVM": SVC()
}

# Results
for vec_name, vectorizer in vectorizers.items():
    print(f"\n=== {vec_name} ===")
    X_train = vectorizer.fit_transform(X_train_text)
    X_test = vectorizer.transform(X_test_text)

    for model_name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        print(f"\n--- {model_name} ---")
        print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))
        print(classification_report(y_test, y_pred))
