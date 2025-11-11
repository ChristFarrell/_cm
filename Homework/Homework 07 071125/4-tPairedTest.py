from scipy.stats import ttest_rel

before = [70, 72, 68, 65, 74]
after = [85, 88, 74, 82, 79]

t_stat, p_value = ttest_rel(before, after)
print(f"t = {t_stat:.3f}") 
print(f"p = {p_value:.4f}")