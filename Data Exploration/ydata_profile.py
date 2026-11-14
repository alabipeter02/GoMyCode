import os
import webbrowser

import pandas as pd
from ydata_profiling import ProfileReport

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#Reading the dataset
Popular_baby_names_df = pd.read_csv("Popular_Baby_Names.csv")

df = pd.DataFrame(Popular_baby_names_df)

# print(f'First 10 Rows: \n{df.head()}')
# print(f'Last 10 Rows: \n{df.tail()}')
# print(df.columns)
# print(df.shape)
# (df.info())
# print(df.describe())

# #Generating a Profile Report
# profile = ProfileReport(df,title="Popular Baby Names Profiling Report", explorative=True)
#
# #To display the report in a Jupyter Notebook
# # profile.to_notebook_iframe()
#
# #Exporting to an HTML file
# output_file = "Popular_Baby_Names_Profiling_Report.html"
# profile.to_file(output_file)
#
# #Open the report in the default web browser
# webbrowser.open('file://' + os.path.abspath(output_file))
#
# #Correlation analysis between Rank and Count columns
# df[["Rank", "Count"]].head()
#
# newCorr = df[["Rank", "Count"]].corr(method="pearson")
# print(newCorr)


#Data Profiling with ydata-profiling for a bank dataset
#bank_df = pd.read_csv("bank-additional-full.csv", sep=';')
# print(bank_df.head())
# print(bank_df.columns)
# print(bank_df.shape)
# (bank_df.info())
# print(bank_df.describe())

# profile = ProfileReport(bank_df, title="Bank Dataset Profiling Report", explorative=True)
#
# #Export to HTML
# output_file = "index.html"
# profile.to_file(output_file)
#
# #Open the report in the default web browser
# webbrowser.open('file://' + os.path.abspath(output_file))

#Data Profiling with ydata-profiling for a Tanzania tourism dataset
tourism_df = pd.read_csv("Historical data of Tanzania Tourism.csv")
print(tourism_df.head())
print(tourism_df.columns)
print(tourism_df.shape)
(tourism_df.info())
print(tourism_df.describe())

profile = ProfileReport(tourism_df, title="Tanzania Tourism Dataset Profiling Report", explorative=True)

#Export to HTML
output_file = "Tanzania_Tourism_Profiling_Report.html"
profile.to_file(output_file)

#Open the report in the default web browser
webbrowser.open('file://' + os.path.abspath(output_file))