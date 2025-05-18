import matplotlib.pyplot as plt

# Sample data: student exam scores
scores = [55, 60, 65, 70, 70, 72, 75, 75, 78, 80, 80, 80, 85, 88, 90]

# Create histogram
plt.hist(scores, bins=5, color='purple', edgecolor='black')

# Add labels and title
plt.title("Distribution of Exam Scores")
plt.xlabel("Score Ranges")
plt.ylabel("Number of Students")

# Show plot
plt.grid(True)
plt.show()
