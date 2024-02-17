import matplotlib.pyplot as plt

# Lists to store data
t_values = []
y_values = []

# Read data from the file
with open("output_data.txt", "r") as file:
    next(file)  # skip the header line
    for line in file:
        t, y = map(float, line.split())
        t_values.append(int(t))
        y_values.append(y)

# Plotting
plt.stem(t_values, y_values, markerfmt='o', linefmt='-',basefmt='-')
plt.title('y(t) vs t')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.xticks(range(0, 101,5))  # Set x-axis ticks for values from 0 to 100
plt.grid(True)
plt.savefig('fig_plot.png')
plt.show()
