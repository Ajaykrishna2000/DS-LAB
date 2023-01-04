# Pandas Dataframe to calculate our z-scores
import pandas as pd
import scipy.stats as stats

df = pd.DataFrame.from_dict({
    'Name': ['Albert', 'Nivin', 'Joe', 'Maya', 'Aleena'],
    'Age': [32, 30, 67, 34, 20],
    'Income': [80000, 90000, 45000, 23000, 12000],
    'Education': [5, 7, 3, 4, 4]
})
print(df.head())

print('\n\nAfter Calculating ZScore:')
df['Income zscore'] = stats.zscore(df['Income'])
print(df.head())

print('\n\nAfter applying "apply()" method:')
df = df.select_dtypes(include='number').apply(stats.zscore)
print(df.head())