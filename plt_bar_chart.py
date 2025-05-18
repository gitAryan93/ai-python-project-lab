import matplotlib.pyplot as plt

# Sample data
students = ["Zaid", "John", "Smith", "Solomon"]
scores = [88, 75, 92, 80]

# Create a bar chart
plt.bar(students, scores, color="green")

# Add title and axis labels
plt.title("Student Score Comparison")
plt.xlabel("Students")
plt.ylabel("Scores")

# Display the chart
plt.show()
