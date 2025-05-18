import pandas as pd

# Sample DataFrame for grouping and missing data
data = {
    "Student": ["John", "Zaid", "John", "Zaid", "John"],
    "Subject": ["Math", "Math", "Science", "Science", "History"],
    "Score": [90, 85, 88, 80, None]
}
df = pd.DataFrame(data)

# === Grouping & Aggregation ===
print("\n=== Average Score by Student ===")
print(df.groupby("Student")["Score"].mean())

print("\n=== Average Score by Subject ===")
print(df.groupby("Subject")["Score"].mean())

# === Handling Missing Data ===
print("\n=== Check for missing values ===")
print(df.isna())

print("\n=== Drop rows with missing values ===")
print(df.dropna())

print("\n=== Fill missing values with 0 ===")
print(df.fillna(0))

print("\n=== Fill missing values with column mean ===")
mean_score = df["Score"].mean()
df["Score_filled"] = df["Score"].fillna(mean_score)
print(df)
