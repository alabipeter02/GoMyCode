import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

tourism = pd.read_csv("Historical data of Tanzania Tourism.csv")

# print(tourism.shape)
# print(tourism.head())
# print(tourism.info())
# print(tourism.isna().sum().sort_values(ascending=False))  #To check the missing values in the dataset

#Finding and cleaning duplicates from the dataset
# print(tourism.duplicated().sum())

#Summary statistics of the dataset
# print(tourism.describe(include='all'))
# print(tourism.describe())

#Creating a correlation heatmap to visualize the correlation between numerical features

numeric = tourism.select_dtypes(include='number')
correlation = numeric.corr()
plt.figure(figsize=(10,7))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
# plt.title('Correlation Heatmap')
# plt.tight_layout()
# plt.show()

#Most common country
top_countries = (
    tourism["country"]
    .value_counts()
    .head(3)
)

# print(top_countries)

#Finding visit purpose by age group
purpose_counts = (
    tourism
    .groupby("age_group")["purpose"]
    .value_counts()
)


most_common = (
    purpose_counts.groupby(level=0)
    .head(1)
)

# print(most_common)


#Analyzing tourist expenditure by country
print(
    tourism.groupby("country")[
        "total_cost"
    ].agg(["count", "mean", "median"])
)

#Analyzing tourist expenditure sorted by country
expenditure_by_country = (
    tourism.groupby("country")["total_cost"]
    .agg(["count", "mean", "median"])
    .sort_values(by="count", ascending=False)
)
print(expenditure_by_country)
#
# #most country highest expenditure
# highest_expenditure_country = (
#     tourism.groupby("country")["total_cost"]
#     .mean()
#     .sort_values(ascending=False)
#     .head(1)
# )
# print(highest_expenditure_country)
