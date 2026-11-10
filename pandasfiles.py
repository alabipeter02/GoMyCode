import numpy as np
import pandas as pd

# numbers = np.array([10, 20, 30])
# scores = pd.Series(numbers)
# print(numbers)
# print(scores)
#
# #Setting my index manually
# students = pd.Series(
#     [75,82,91],
# index=["Ada", "John", "John"]
# )
# print(students)
# print(students["John"])
#
# #Creating series from a list
# products = ['A', 'B', 'C', 'D']
# products_series = pd.Series(products)
# print(type(products))
# print(type(products_series))

#Defining the colors and their occurrences
colors = ['pink', 'white', 'black', 'blue']
occurrences = [20, 15, 6, 43]
#creating the series with a custom index
color_series = pd.Series(occurrences, index=colors)
#print(color_series)

#Series addition
# Define the colors and their corresponding values in two different series
colors = ['pink', 'white', 'black', 'blue']
S1 = pd.Series([20, 15, 6, 43], index=colors)
S2 = pd.Series([3, 22, 9, 10], index=colors)
#Adding the two series
result = S1 + S2
#print(result)

#Pandas DataFrame
data = {
    'Name': ['Ada', 'John', 'Mary'],
    'Age': [22, 25, 21],
    'Score': [85.5, 78.0, 92.0]}
df = pd.DataFrame(data)
#print(df)

#Creating dataframe for custom indexes
data = {
    "Name": ["Peter", "Victoria", "David"],
    "Age": [30, 28, 32],
    "City": ["Lagos", "Abuja", "Ibadan"]}

df = pd.DataFrame(data,index=["A", "B", "C"])
#print(df)

#Accessing Element using the index
#print(df.loc['B'])  # Accessing row with index 'B'

#Data Alignment
names = pd.Series(['Ada', 'John'], index=[0,1])
scores = pd.Series([90, 75], index=[1,0])
df = pd.DataFrame({'Name': names, 'Score': scores})
#print(df)

#print(df)

#Selecting a specific column
#print(df['Name'])

#Selecting multiple columns
#print(df[['Name', 'Age']])

#Selecting a specific row
#print(df.loc[0])

#Selecting a specific element
#print(df.loc[0, 'Name'])


#Data Selection in Pandas
data = {
    'Name': ['John', 'Jack', 'Angelina', 'Andrew'],
    'Age': [23, 20, 21, 22],
    'Home Address': [
         'Los Angeles',
         'California',
         'New York',
         'Florida'
    ]
}
df = pd.DataFrame(data)
new_data = df[['Age', 'Home Address']]
#print(df)
#print(new_data)

#Example 2: Selecting specific columns from a DataFrame
data = {
    'Name': ['Ada', 'John', 'Mary', 'David'],
    'Age': [22, 25, 21, 23],
    'Home Address': [
        'Lagos',
        'Abuja',
        'Ibadan',
        'Port Harcourt'
    ]
}
df = pd.DataFrame(data)
new_data = df[['Name', 'Age']]
# print(df)
# print(new_data)

#Loc Selection
df = pd.DataFrame({
    'Age': [20, 3, 21,22],
    'Role':['AI', 'AI', 'WEB1', 'WEB2'],
})
df.index = ['Jack', 'Thomas', 'Alexandre', 'Anne']
selected_data = df.loc[['Jack', 'Thomas']]
#print(selected_data)

#iloc Selection
df = pd.DataFrame({
    'Name': ['John', 'Jack', 'Angelina', 'Andrew'],
    'Last Name': ['Stott', 'Mcbride', 'Newman', 'Hines'],
    'Age': [23, 20, 21, 22],
    'Role':['AI', 'AI', 'WEB1', 'WEB2'],
    'Home Address': [
        'Los Angeles',
        'California',
        'New York',
        'Florida'
    ]
})
selected_columns = df.iloc[:, 1:3]  # Selecting the first and third columns
# print(df)
# print(selected_columns)

#Exercise
product_list = ['Apple', 'Banana', 'Carrot', 'Daikon']

#Convert the list to series
product = pd.Series(product_list)
print(product)

# #Creating a series containing the prices of the products
price_list = [2, 1, 3, 4]
prices = pd.Series(price_list)
print(prices)

# #Combining the two series side by side
combined = pd.concat([product, prices], axis=1)
print(combined)

#Create a DataFrame containing the product names and their prices
data = {
    'Product': product,
    'Price': prices
}
df = pd.DataFrame(data)
print(df)

# #Create a DataFrame using a dictionaries
data = [
    {"Product": "Apple", "Price": 2},
    {"Product": "Banana", "Price": 1},
    {"Product": "Carrot", "Price": 3},
    {"Product": "Daikon", "Price": 6}
]

df = pd.DataFrame(data)
print(df)  
