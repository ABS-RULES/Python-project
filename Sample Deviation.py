import numpy as np
import scipy.stats as stats

marks = [8, 16, 20, 16, 32, 13, 17, 20, 25, 16, 23, 16, 25, 22, 1, 7, 40, 30, 13, 10, 26, 31, 18, 15, 32]

mean = np.mean(marks)

squared_deviations = [(x - mean) ** 2 for x in marks]
sample_variance = np.sum(squared_deviations) / (len(marks) - 1)

chi_square_95_lower = 39.364
chi_square_95_upper = 12.401
chi_square_99_lower = 44.314
chi_square_99_upper = 11.688

n = len(marks)

variance_95_lower = ((n - 1) * sample_variance) / chi_square_95_upper
variance_95_upper = ((n - 1) * sample_variance) / chi_square_95_lower

variance_99_lower = ((n - 1) * sample_variance) / chi_square_99_upper
variance_99_upper = ((n - 1) * sample_variance) / chi_square_99_lower

print(f"Sample Variance (s^2): {sample_variance:.2f}")
print(f"95% Confidence Interval for Population Variance (σ^2): ({variance_95_lower:.2f}, {variance_95_upper:.2f})")
print(f"99% Confidence Interval for Population Variance (σ^2): ({variance_99_lower:.2f}, {variance_99_upper:.2f})")
