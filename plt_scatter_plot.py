import matplotlib.pyplot as plt

# Sample data
hours_studied = [1, 2, 3, 4, 5, 6]
exam_scores = [55, 60, 65, 70, 78, 85]

# Create scatter plot
plt.scatter(hours_studied, exam_scores, color="red", marker="x")

# Add title and labels
plt.title("study Time vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")

# Show grid and plot
plt.grid(True)
plt.show()
