import matplotlib.pyplot as plt

# Read data from the file
with open("output_data.txt", "r") as file:
    lines = file.readlines()

# Extracting n and y(n) values
n_values = []
y_values = []
for line in lines[1:]:  # Skip the header line
    n, y_n = line.split()
    n_values.append(int(n))
    y_values.append(float(y_n))

# Plotting
plt.figure(figsize=(8, 6))
plt.stem(n_values, y_values, basefmt='b-')
plt.title("Stem Plot of y(n) vs. n")
plt.xlabel("n")
plt.ylabel("y(n)")
plt.xticks(range(0,16))
plt.grid(True)
plt.savefig('figure_plot.png')
plt.show()
