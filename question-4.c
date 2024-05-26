#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// Function to generate uniform random numbers between 0 and 1
double uniform_random() {
    return (double)rand() / (double)RAND_MAX;
}

// Function to generate exponential random numbers with mean 0.5
double exponential_random(double lambda) {
    double u = uniform_random();
    return -log(u) / lambda;
}

int main() {
    const int n = 10000;
    double lambda = 2.0; // mean = 1/lambda = 0.5
    double random_numbers[n];

    // Seed the random number generator
    srand(time(NULL));

    // Generate 10,000 exponential random numbers
    for (int i = 0; i < n; i++) {
        random_numbers[i] = exponential_random(lambda);
    }

    // Write the numbers to a file
    FILE *f = fopen("exponential_random_numbers.txt", "w");
    if (f == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    for (int i = 0; i < n; i++) {
        fprintf(f, "%f\n", random_numbers[i]);
    }
    fclose(f);

    printf("Generated 10,000 exponential random numbers and saved to exponential_random_numbers.txt\n");
    return 0;
}
