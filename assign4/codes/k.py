import matplotlib.pyplot as plt

# Read data from the output_data.txt file
with open("output_data.txt", "r") as file:
    data = file.readlines()

# Extract t, x(t), and y(t) from the data
t = []
x_t = []
y_t = []
for line in data[1:]:  # Skip the header
    values = line.split()
    t.append(float(values[0]))
    x_t.append(float(values[1]))
    y_t.append(float(values[2]))

# Create a continuous plot for x(t)
plt.plot(t, x_t, 'b-', label='x(t)')

# Create a continuous plot for y(t)
plt.plot(t, y_t, 'r-', label='y(t)')

# Add labels and legend
plt.xlabel('t')
plt.ylabel('y(t), x(t)')
plt.legend()
plt.xticks(range(0, 101, 5))  # Set x-axis ticks for values from 0 to 100
plt.grid(True)

# Save and display the plot
plt.savefig('fig_plot.png')
plt.show()
