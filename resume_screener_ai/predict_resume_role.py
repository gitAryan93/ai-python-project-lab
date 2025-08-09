import os
import pandas as pd
import pickle
from .resume_cleaner import clean_resume_data

# Set current directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load saved model and vectorizer
with open(os.path.join(CURRENT_DIR, "model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(CURRENT_DIR, "vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)

# Load new resumes (raw)
# ← use new test resumes here
resume_path = os.path.join(CURRENT_DIR, "resumes.csv")
df_raw = pd.read_csv(resume_path)

# Clean the resume text
df_cleaned = clean_resume_data(resume_path)

# Vectorize the cleaned text
X_input = vectorizer.transform(df_cleaned["cleaned_text"])

# Predict using the model
predictions = model.predict(X_input)

# Add predictions to the DataFrame
df_cleaned["predicted_role"] = predictions

# Save the result
output_path = os.path.join(CURRENT_DIR, "predicted_resumes.csv")
df_cleaned.to_csv(output_path, index=False)

print("✅ Prediction complete. Results saved to predicted_resumes.csv")
print(df_cleaned[["resume", "predicted_role"]])
