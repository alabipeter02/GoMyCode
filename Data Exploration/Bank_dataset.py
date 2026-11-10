import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('bank-additional-full.csv',
sep=';')

print(df.shape)
# print(df.head())
# print(df.info())
# print(df.columns)

print(df.describe())

#Q1: Calculating the subscription share
print(df['y'].value_counts())

print(df['y'].value_counts(normalize=True) * 100)

#Analyzing the subscribers
subscribers = df[df['y'] == 'yes']

print(subscribers.select_dtypes(include='number').mean())

#Calculating the average age of unmarried subscribers
unmarried_subscribers = df[(df['y'] == 'yes') & (df['marital'] == 'single')]

print(unmarried_subscribers['age'].mean())

#Comparing job categories
job_summary = df.groupby('job').agg(
    average_age=('age','mean'),
    average_duration=('duration','mean'),
    clients=('job', 'size'))

print(job_summary)

 