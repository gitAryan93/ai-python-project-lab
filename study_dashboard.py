import pandas as pd

data = {
    'date': ['2025-05-18', '2025-05-18', '2025-05-19', '2025-05-20', '2025-05-20', '2025-05-21'],
    'subject': ['Python', 'Math', 'Python', 'AI', 'Math', 'Python'],
    'hours': [2, 1, 3, 2, 1.5, 2.5],
    'focus_level': [8, 7, 9, 6, 7, 8]  # Scale of 1 to 10
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Basic summaries
total_hours = df['hours'].sum()
avg_focus = df['focus_level'].mean()
top_subject = df['subject'].value_counts().idxmax()

# Output summaries
print("===== Study Dashboard Summary =====")
print("Total Study Hours:", total_hours)
print("Average Focus Level:", round(avg_focus, 2))
print("Most Frequent Subject Studied:", top_subject)

# Daily summary
daily_hours = df.groupby('date')['hours'].sum()
print("\nDaily Study Hours:\n", daily_hours)

# Subject summary
subject_hours = df.groupby('subject')['hours'].sum()
print("\nHours by Subject:\n", subject_hours)
