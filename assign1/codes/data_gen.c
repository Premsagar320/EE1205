#include <stdio.h>
#include <math.h>

int main() {
    FILE *file;
    file = fopen("output_data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Print headers
    fprintf(file, "n     x(n)\n");

    // Given values
    double a = 2.0; // Replace with your desired value
    double r = 3.0; // Replace with your desired value

    // Generate values for n to cover the range from -10 to 10 (inclusive) with a step of 1
    for (int n = -10; n <= 10; n++) {
        // Calculate and write to file
        fprintf(file, "%d %lf\n", n, (n >= 0) ? a * pow(r, n) : 0.0);
    }

    fclose(file);

    return 0;
}
 
