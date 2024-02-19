# import the required libraries
import random
import matplotlib.pyplot as plt

# store the random numbers in a
# list
nums = []
mu = 100
sigma = 50

for i in range(100):
    temp = max(0,random.gauss(mu, sigma))
    nums.append(temp)

# plotting a graph
plt.plot(nums)
plt.show()
print(random.gauss(mu, sigma))