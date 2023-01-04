# Calculate the z-score from with scipy
import scipy.stats as stats
values = [4, 5, 6, 6, 6, 7, 8, 12, 13, 13, 14, 18]

zscores = stats.zscore(values)
print(zscores)