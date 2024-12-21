import numpy as np
from scipy import stats

treated = [3.7, 2.8, 4.6, 4.4, 2.76, 3.67, 4.14, 2.89, 3.79, 4.09, 2.56, 3.12, 4.64, 3.78, 3.46]
untreated = [0.5, 1.9, 2.8, 3.1, 0.75, 1.68, 3.25, 3.56, 1.08, 1.75]

mean_treated = np.mean(treated)
mean_untreated = np.mean(untreated)
var_treated = np.var(treated, ddof=1)  
var_untreated = np.var(untreated, ddof=1)  

n_treated = len(treated)
n_untreated = len(untreated)

Sp = np.sqrt(((n_treated - 1) * var_treated + (n_untreated - 1) * var_untreated) / (n_treated + n_untreated - 2))

t_stat = (mean_treated - mean_untreated) / (Sp * np.sqrt(1/n_treated + 1/n_untreated))

df = n_treated + n_untreated - 2

alpha = 0.05
t_critical = stats.t.ppf(1 - alpha/2, df)

print(f"T-statistic: {t_stat:.4f}")
print(f"Critical t-value: {t_critical:.4f}")

if abs(t_stat) > t_critical:
    print("Decision: H0 is Rejected")
    print("Ha is Accepted")
else:
    print("Decision: H0 is Accepted")
    print("Ha is Rejected")
    