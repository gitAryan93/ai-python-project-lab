import matplotlib.pyplot as plt

# Use a built-in style
# Try also: "seaborn", "fivethirtyeight", "dark_background"
plt.style.use("ggplot")

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 15, 9]

# Plot with style
plt.plot(x, y, marker="o", color="teal", label="Growth")

# Add title and lables
plt.title("Styled Line Chart")
plt.xlabel("time")
plt.ylabel("Value")

# Add grid and legend
plt.grid(True)
plt.legend()

# Save plot to file
plt.savefig("styled_line_chart.png")  # Saves to your project folder

# Show it
plt.show()
