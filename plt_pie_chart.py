import matplotlib.pyplot as plt

# Data
labels = ["Python", "Java", "C++", "JavaScript"]
usage = [40, 25, 20, 15]
colors = ["#66b3ff", "#99ff99", "#ffcc99", "#ff9999"]

# Create pie chart
plt.pie(usage, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)

# Add title and equal axis
plt.title("Programing Language Usage")
plt.axis("equal")  # Keeps the pie circular

# Display chart
plt.show()
