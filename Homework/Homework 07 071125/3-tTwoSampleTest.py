from scipy.stats import ttest_ind

sains = [82, 85, 88, 90, 79]
social = [75, 78, 84, 80, 76]

t_stat, p_value = ttest_ind(sains, social)
print(f"t = {t_stat:.3f}") 
print(f"p = {p_value:.4f}")