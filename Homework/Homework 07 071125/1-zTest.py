import math
from scipy.stats import norm
import numpy as np

mu = 170      # avaerage of population
sigma = 10    # population standard deviation

# Sample data
sample = np.array([172, 174, 179, 185, 171, 173, 174, 178, 170, 172])
n = len(sample)
x_bar = np.mean(sample)

# Compute z statistic
z = (x_bar - mu) / (sigma / math.sqrt(n))

# Two-tailed p-value
p = 2 * (1 - norm.cdf(abs(z)))

print(f"z = {z:.3f}")
print(f"p = {p:.4f}")

