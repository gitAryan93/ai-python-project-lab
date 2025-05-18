import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [5, 10, 8, 12, 7]

# Create a simple line chart
plt.plot(x, y, marker="o", linestyle="-", color="blue", label="Data Line")

# Add title and labels
plt.title("Line Chart Example")
plt.xlabel("X Axis - Days")
plt.ylabel("Y Axis - Value")

# Show legend and grid
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
