import matplotlib.pyplot as plt

# Lists to store data
n_values = []
y_values = []

# Read data from the file
with open("output_data.txt", "r") as file:
    next(file)  # skip the header line
    for line in file:
        n, y = map(float, line.split())
        n_values.append(int(n))
        y_values.append(y)

# Plotting
plt.stem(n_values, y_values, markerfmt='o', linefmt='-',basefmt='-')
plt.title('y(n) vs n')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.xticks(range(0, 16))  # Set x-axis ticks for values from 0 to 15
plt.grid(True)
plt.savefig('figure_plot.png')
plt.show()
