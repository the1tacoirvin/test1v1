import random
import math


def generate_rock_size():
    # Assuming the rock sizes follow a normal distribution
    mean = random.uniform(0.5, 2.0)  # Mean rock size between 0.5 and 2.0 inches
    stddev = random.uniform(0.1, 0.5)  # Standard deviation between 0.1 and 0.5 inches
    return max(0, random.gauss(mean, stddev))  # Ensuring rock size is non-negative


def sieve_rock(rock_size):
    # Checking if the rock can pass through the 3/8"x3/8" mesh screen
    if rock_size <= 3 / 8:
        # Checking if the rock is too big to fit through the 1"x1" mesh screen
        if rock_size > 1:
            return True  # Rock is retained
    return False  # Rock passes through


def sample_rocks(sample_size):
    rocks = [generate_rock_size() for _ in range(sample_size)]
    return rocks


def report_statistics(samples):
    sample_means = [sum(sample) / len(sample) for sample in samples]
    sample_variances = [sum((x - mean) ** 2 for x in sample) / len(sample) for sample, mean in
                        zip(samples, sample_means)]

    print("Sample Means:")
    for mean in sample_means:
        print(mean)

    print("\nSample Variances:")
    for variance in sample_variances:
        print(variance)

    overall_mean = sum(sample_means) / len(sample_means)
    overall_variance = sum(sample_variances) / len(sample_variances)
    print("\nOverall Mean of Sample Means:", overall_mean)
    print("Overall Variance of Sample Means:", overall_variance)


def simulate_rock_crushing(num_samples, sample_size):
    samples = [sample_rocks(sample_size) for _ in range(num_samples)]
    report_statistics(samples)


if __name__ == "__main__":
    num_samples = 11
    sample_size = 100
    simulate_rock_crushing(num_samples, sample_size)
