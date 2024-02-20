#include <stdio.h>
#include <math.h>  // Include math.h for fmod function

// Define the function x(t) with a fundamental period of 100 seconds
double x(double t) {
    double period = 100.0;  // Fundamental period of x(t) in seconds
    double normalized_t = fmod(t, period);  // Normalize t within one period
    return sin(2 * M_PI * t / 100);  // Example function: sin(2πt/100)
}

int main() {
    FILE *file;
    file = fopen("output_data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Print headers
    fprintf(file, "t  x(t)   y(t)\n");

    // Given values
    double t, x_t, y_t;  // Values of t, x(t), and y(t)

    // Generate values for t to cover the range from 0 to 100 (inclusive) with a step of 5
    for (t = 0; t <= 100; t += 5) {
        // Calculate x(t)
        x_t = x(t);

        // Calculate y(t) = x(4t)
        y_t = x(4 * t);

        // Write to file
        fprintf(file, "%.2lf  %.2lf %.2lf\n", t, x_t, y_t);
    }

    fclose(file);

    return 0;
}
