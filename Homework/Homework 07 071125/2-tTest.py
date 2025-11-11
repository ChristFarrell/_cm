import numpy as np
from scipy.stats import ttest_1samp

scores = np.array([78, 74, 80, 72, 76, 79, 73])
mu = 75  # hypothesized mean

t_stat, p_value = ttest_1samp(scores, mu)
print(f"t = {t_stat:.3f}") 
print(f"p = {p_value:.4f}")