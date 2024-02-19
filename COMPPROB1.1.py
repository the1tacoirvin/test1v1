import random
import copy

def sample_mean(sample):
    '''does the value for the mean via finding the sum of all samples found in the sample_size '''
    return sum(sample) / len(sample) if len(sample) > 0 else 0  # Add a check for the length of the sample

def sample_variance(sample):
    '''does the value for the variance via finding the sum of all samples found in the sample_size into an equation'''
    mean = sample_mean(sample)
    return sum((x - mean) ** 2 for x in sample) / len(sample) if len(sample) > 0 else 0  # Add a check for the length of the sample

def main():
    '''time to print everything, and the math, lots of math'''
    num_samples = 11 #how many times we want to fine a mean and variance.
    sample_size = 100 #how many rocks in each trial,
    samples = [] #starts the list to hold the values found.

    for _ in range(num_samples):
        rocks = [max(0, random.gauss(0.6875, 2.5)) for _ in range(sample_size)]
        '''according to my simple research, some gravel can be 10 inches in diameter to still be considered gravel, thus I threw in the chance 
        that the rocks could be 10 inches, however you can't have a negative rock so I put a max value'''
        sample = [rock for rock in rocks if 1 >= rock >= 3/8]  # Filter rocks between 1" and 3/8", anything outside this range just doesn't work
        samples.append(copy.deepcopy(sample)) #copys the number

    sample_means = [sample_mean(sample) for sample in samples] #repeats the for_in thing above till 100 samples have been collected, changing the numper each time.
    #goes back the sample_mean funtion to put the number found, getting a number, and repeating everything until we have 11 samples
    sample_variances = [sample_variance(sample) for sample in samples] #repeats the for_in thing above till 100 samples have been collected, changing the number each time
    # goes back the sample_variance funtion to put the number found, getting a number, and repeating everything until we have 11 samples
    print("Sample Mean and Variance of each sample:")
    for i in range(num_samples):
        print(f"Sample {i+1}: Mean = {sample_means[i]}, Variance = {sample_variances[i]}")
        '''does this for each of the 11 samples, just so we can see the numbers and trouble shoot'''

    print("\nMean and Variance of the sampling mean:")
    mean_of_means = sum(sample_means) / num_samples
    '''gets the sum of all sample means divided by 11 so we can get well, the mean of everything'''
    variance_of_means = sum(sample_variances)/ num_samples
    '''gets the sum of all sammple_variance_of_means divided by 11 so we can get well, the mean of everything'''
    print(f"Mean of Sampling Mean: {mean_of_means}")
    print(f"Variance of Sampling Mean: {variance_of_means}")

if __name__ == "__main__":
    main()
