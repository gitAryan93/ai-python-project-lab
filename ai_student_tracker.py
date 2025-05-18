import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === 1. Create Dataset ===
data = {
    "Student": ["Smith", "John", "Zaid", "Solomon", "Michael", "Sam"],
    "Hours_Studied": [12, 15, 10, 9, np.nan, 8],
    "Exercises_Completed": [30, 40, 25, 20, 35, 15],
    "Final_Score": [85, 92, 78, 70, 88, 60]
}
df = pd.DataFrame(data)

# === 2. Clean & Add Calculated Column ===
df["Hours_Studied"] = df["Hours_Studied"].fillna(df["Hours_Studied"].mean())
df["Passed"] = df["Final_Score"] >= 75

# === 3. Print Cleaned DataFrame ===
print("=== Cleaned DataFrame ===")
print(df)

# === 4. Visualizations ===

# Line Chart: Hours Studied
plt.figure(figsize=(8, 5))
plt.plot(df["Student"], df["Hours_Studied"], marker='o', color='blue')
plt.title("Hours Studied by Student")
plt.xlabel("Student")
plt.ylabel("Hours Studied")
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Chart: Final Scores
plt.figure(figsize=(8, 5))
plt.bar(df["Student"], df["Final_Score"], color='green')
plt.title("Final Score by Student")
plt.xlabel("Student")
plt.ylabel("Final Score")
plt.tight_layout()
plt.show()

# Pie Chart: Pass/Fail Distribution
pass_counts = df["Passed"].value_counts()
labels = ["Passed", "Failed"]
plt.figure(figsize=(6, 6))
plt.pie(pass_counts, labels=labels, autopct="%1.1f%%",
        startangle=90, colors=["#66b3ff", "#ff9999"])
plt.title("Pass/Fail Distribution")
plt.axis("equal")
plt.tight_layout()
plt.show()

# Histogram: Hours Studied
plt.figure(figsize=(8, 5))
plt.hist(df["Hours_Studied"], bins=5, color='purple', edgecolor='black')
plt.title("Distribution of Hours Studied")
plt.xlabel("Hours")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter Plot: Exercises vs Final Score
plt.figure(figsize=(8, 5))
plt.scatter(df["Exercises_Completed"],
            df["Final_Score"], color='red', marker='x')
plt.title("Exercises Completed vs Final Score")
plt.xlabel("Exercises Completed")
plt.ylabel("Final Score")
plt.grid(True)
plt.tight_layout()
plt.show()
