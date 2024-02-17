#include <stdio.h>
#include <math.h>  // Include math.h for fmod function

// Define the function x(t) with a fundamental period of 100 seconds
double x(double t) {
    double period = 100.0;  // Fundamental period of x(t) in seconds
    double normalized_t = fmod(t, period);  // Normalize t within one period
    return normalized_t * normalized_t;  // Example function: t^2
}

int main() {
    FILE *file;
    file = fopen("output_data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Print headers
    fprintf(file, "t     y(t)\n");

    // Given values
    double t, y_t;  // Values of t and y(t)

    // Generate values for t to cover the range from 0 to 100 (inclusive) with a step of 5
    for (t = 0; t <= 100; t += 5) {
        // Calculate y(t) = x(4t)
        y_t = x(4 * t);

        // Write to file
        fprintf(file, "%.2lf %.2lf\n", t, y_t);
    }

    fclose(file);

    return 0;
}
 
