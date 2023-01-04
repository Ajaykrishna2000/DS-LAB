import numpy as np

def normalize(x):
    min = np.min(x)
    max = np.max(x)
    range = max-min

    return [(a-min) / range for a in x]

x = [5, 12, 18, 25]
normalizedX = normalize(x)
print(normalizedX)