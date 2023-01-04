import scipy.stats as stats
values = [4, 1, 6, 6, 5, 8, 12, 13, 3, 14, 18]

# Calculate the Standard Deviation in Python
mean = sum(values) / len(values)
differences = [(value - mean)**2 for value in values]
sum_of_differences = sum(differences)
standard_deviation = (sum_of_differences / (len(values) - 1)) ** 0.5

print(standard_deviation)