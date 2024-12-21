import numpy as np
import matplotlib.pyplot as plt

# Data
marks = [8, 16, 13, 38, 21, 13, 25, 7, 33, 2, 23, 22, 21, 37, 16, 7, 13, 20, 20, 5,
         26, 15, 28, 20, 16, 32, 27, 36, 17, 16, 14, 30, 16, 1, 8, 28, 40, 10, 1, 33,
         31, 32, 36, 2, 20, 32, 20, 4, 20, 25, 16, 21, 25, 6, 3, 14, 30, 4, 22, 21,
         18, 18, 38, 8]

mu = 20.78  
sigma = 9.43  


range_1 = (mu - sigma, mu + sigma)
range_2 = (mu - 2 * sigma, mu + 2 * sigma)
range_3 = (mu - 3 * sigma, mu + 3 * sigma)

plt.hist(marks, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.axvline(mu, color='red', linestyle='dashed', linewidth=1, label='Mean (μ)')
plt.axvline(range_1[0], color='blue', linestyle='dashed', linewidth=1, label='±1σ')
plt.axvline(range_1[1], color='blue', linestyle='dashed', linewidth=1)
plt.axvline(range_2[0], color='green', linestyle='dashed', linewidth=1, label='±2σ')
plt.axvline(range_2[1], color='green', linestyle='dashed', linewidth=1)
plt.axvline(range_3[0], color='purple', linestyle='dashed', linewidth=1, label='±3σ')
plt.axvline(range_3[1], color='purple', linestyle='dashed', linewidth=1)
plt.legend()
plt.show()