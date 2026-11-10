import numpy as np
import pandas as pd
from scipy import stats
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
#pd.set_option('display.max_info_columns', None)


data = pd.read_csv("Popular_Baby_Names.csv")

df = data.rename(columns={
    "Child's First Name": 'First_Name',
    'Year of Birth': 'Year',
})

#Filtering for male entries from the year 2015
# df_filtered = df.query('Year > 2015 and Gender == "MALE"')
# df_filtered.head()

# print(df_filtered)
# print(df)
# print(data)

#Creating a new column with the assign Function to the dataframe
df_new = df.assign(Name_Length = df["First_Name"].apply(len))
#print(df_new)


#Data sorting by the new column Name_Length in descending order
df_sorted = df_new.sort_values(by='Name_Length', ascending=False)
#print(df_sorted)

#Saving the sorted data to a new CSV file
# df_sorted.to_csv("Sorted_Popular_Baby_Names.csv", index=False)

#Creating DataFrame with the missing values
data = {
    "A": [1, 2, np.                                                                                       nan, 4, 5],
    "B": [np.nan, 2, 3, 4, 5],
    "C": [1, 2, 3, np.nan, 5],
    "D": [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

#print(df)

#Detecting outliers with Z-score method
df = pd.DataFrame({
     "Height": [
         170, 160, 130,190,180,
         150, 140, 200, 175, 165
]})
z_scores = np.abs(stats.zscore(df['Height']))

#outliers = df[z_scores > 3]
#print(outliers)

#Detecting outliers with IQR method
Q1 = df['Height'].quantile(0.25)
Q3 = df['Height'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[
    (df["Height"] < lower) |
    (df["Height"] > upper)
]
# print(outliers)
# print(IQR)

#Handling Duplicate values
df = pd.DataFrame({
    "Name": ["John", "Anna", "John", "Mike"],
    "Age": [28, 22, 28, 20]
})
#print(df.duplicated())

df = df.drop_duplicates()
# print(df)

#Dictionary Mapping
df = pd.DataFrame({
    "Priority": [
        "Low", "Medium", "High",
        "Medium", "Low"]
})
priority_mapping = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}
df["Priority_Score"] = df["Priority"].map(priority_mapping)
# print(df)

#One-hot Encoding
df = pd.DataFrame({
    "Fruit": ["Apple", "Orange", "Banana",
              "Banana", "Orange", "Apple"]
})

one_hot_df = pd.get_dummies(
    df,columns=['Fruit'],
    dtype=int
)
#print(one_hot_df)


#Encoding Categorical Variables with LabelEncoder
fruits = ["Apple", "Avocado", "Banana", "Banana", "Orange", "Kiwi", "Mango", "Apple"]
encoder = LabelEncoder()

encoded = encoder.fit_transform(fruits)
print(encoder.classes_)
print(encoded)

