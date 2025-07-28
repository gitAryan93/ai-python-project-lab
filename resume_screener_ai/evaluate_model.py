import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load labeled cleaned data
df = pd.read_csv("cleaned_labeled_resumes.csv")
X = vectorizer.transform(df['cleaned_text'])
y_true = df['label']

# Predict
y_pred = model.predict(X)

# Evaluation
print("✅ Model Evaluation:")
print("Accuracy:", accuracy_score(y_true, y_pred))
print("\nClassification Report:\n", classification_report(y_true, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_true, y_pred))
