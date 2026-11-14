
# Import required libraries

import requests
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image as PILImage
from io import BytesIO

# print("All libraries imported successfully!")
#
# # Store NASA API key
# API_KEY = "9GwnG96HN6pRjcp6F9bmRmgQwRhJKnhnzfgDpWRQ"
#
# print("NASA API key stored successfully!")
#
#
#
# # STEP 5: Connect to NASA APOD API
#
# url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
#
# params = {
#     "api_key": API_KEY
# }
#
# response = requests.get(url, params=params, timeout=30)
#
# print("Status Code:", response.status_code)
#
# response.raise_for_status()
#
# data = response.json()
#
# # Handle list or dictionary response
# if isinstance(data, list):
#     apod = data[0]
# else:
#     apod = data
#
# # Extract APOD information
# print("Title:", apod["title"])
# print("Date:", apod["date"])
# print("Media Type:", apod["media_type"])
# print("Explanation:", apod["explanation"])
#
#
# # STEP 6: Download and display NASA APOD image
#
# if apod["media_type"] == "image":
#
#     image_url = apod.get("hdurl") or apod.get("url")
#
#     # Download image
#     image_response = requests.get(image_url, timeout=30)
#     image_response.raise_for_status()
#
#     # Check downloaded content
#     print("Content Type:", image_response.headers.get("Content-Type"))
#     print("Image URL:", image_url)
#
#     # Open image using PIL
#     image = PILImage.open(BytesIO(image_response.content))
#
#     # Save image using its actual format
#     image_format = image.format
#     extension = image_format.lower()
#
#     file_name = f"NASA_APOD.{extension}"
#
#     image.save(file_name)
#
#     # Display image
#     plt.figure(figsize=(10, 7))
#     plt.imshow(image)
#     plt.axis("off")
#     plt.title(apod["title"])
#     plt.show()
#
#     print("Image downloaded successfully!")
#     print("Saved as:", file_name)
#
# else:
#     print("Today's APOD is not an image.")
#     print("Media Type:", apod["media_type"])
#
# STEP 7: CONNECT TO NASA ASTEROIDS API

neo_url = "https://api.nasa.gov/neo/rest/v1/feed"

# Get today's date
from datetime import datetime

today = datetime.today().strftime("%Y-%m-%d")

# API parameters
neo_params = {
    "api_key": "9GwnG96HN6pRjcp6F9bmRmgQwRhJKnhnzfgDpWRQ",
    "start_date": today,
    "end_date": today
}

# Send GET request
neo_response = requests.get(
    neo_url,
    params=neo_params
)

# Check response
print("Asteroid API Status Code:", neo_response.status_code)

neo_response.raise_for_status()

# Convert JSON response
neo_data = neo_response.json()

print("Asteroid data retrieved successfully!")

# Display available information
print(neo_data.keys())

# import socket
#
# try:
#     ip_address = socket.gethostbyname("api.nasa.gov")
#     print("NASA IP Address:", ip_address)
#     print("DNS connection successful!")
#
# except socket.gaierror:
#     print("DNS connection failed!")
#     print("Check your internet or DNS settings.")



# STEP 8: EXTRACT ASTEROID DATA INTO DATAFRAME

#Extract asteroid records
asteroid_list = neo_data["near_earth_objects"][today]

# Convert asteroid records into DataFrame
asteroid_df = pd.json_normalize(asteroid_list)

# # Display selected columns
# print(asteroid_df[[
#     "name",
#     "absolute_magnitude_h",
#     "is_potentially_hazardous_asteroid",
#     "estimated_diameter.kilometers.estimated_diameter_min",
#     "estimated_diameter.kilometers.estimated_diameter_max"
# ]])
#
# # Display DataFrame information
# print("\nDataFrame Shape:", asteroid_df.shape)
#
# print("\nDataFrame Columns:")
# print(asteroid_df.columns.tolist())
#
# print("\nFirst 5 Records:")
# print(asteroid_df.head())


# STEP 9: DATA CLEANING AND FEATURE SELECTION

# Select relevant columns
asteroid_clean = asteroid_df[[
    "id",
    "name",
    "absolute_magnitude_h",
    "is_potentially_hazardous_asteroid",
    "estimated_diameter.kilometers.estimated_diameter_min",
    "estimated_diameter.kilometers.estimated_diameter_max"
]].copy()

# Rename columns
asteroid_clean.columns = [
    "Asteroid_ID",
    "Asteroid_Name",
    "Absolute_Magnitude",
    "Potentially_Hazardous",
    "Min_Diameter_KM",
    "Max_Diameter_KM"
]

# Check missing values
print("Missing Values:")
print(asteroid_clean.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(asteroid_clean.duplicated().sum())

# Remove duplicates
asteroid_clean.drop_duplicates(inplace=True)

# Display cleaned dataset
print("\nCleaned Asteroid Dataset:")
print(asteroid_clean.head())

print("\nDataset Shape:", asteroid_clean.shape)



# STEP 10: ASTEROID DATA ANALYSIS

# Total number of asteroids
total_asteroids = len(asteroid_clean)

# Count potentially hazardous asteroids
hazardous_asteroids = asteroid_clean[
    asteroid_clean["Potentially_Hazardous"] == True
].shape[0]

# Count non-hazardous asteroids
non_hazardous = total_asteroids - hazardous_asteroids

# Calculate hazardous asteroid percentage
hazardous_percentage = (
    hazardous_asteroids / total_asteroids * 100
    if total_asteroids > 0 else 0
)

# Calculate average asteroid diameter
average_diameter = asteroid_clean[
    ["Min_Diameter_KM", "Max_Diameter_KM"]
].mean().mean()

# Display analysis
print("NASA ASTEROID ANALYSIS")
print("======================")

print("Total Asteroids:", total_asteroids)
print("Potentially Hazardous:", hazardous_asteroids)
print("Non-Hazardous:", non_hazardous)

print("Hazardous Percentage:",
      round(hazardous_percentage, 2), "%")

print("Average Estimated Diameter:",
      round(average_diameter, 4), "KM")



# STEP 11: DATA VISUALIZATION


# 1. Hazardous vs Non-Hazardous Asteroids
# hazard_counts = asteroid_clean[
#     "Potentially_Hazardous"
# ].value_counts()
#
# plt.figure(figsize=(7, 5))
# hazard_counts.plot(
#     kind="bar",
#     rot=0
# )
# plt.title("Hazardous vs Non-Hazardous Asteroids")
# plt.xlabel("Potentially Hazardous")
# plt.ylabel("Number of Asteroids")
# plt.xticks([0, 1], ["Non-Hazardous", "Hazardous"])
# plt.tight_layout()
# plt.show()
#
#
# # 2. Distribution of Asteroid Diameters
# plt.figure(figsize=(8, 5))
# plt.hist(
#     asteroid_clean["Max_Diameter_KM"],
#     bins=15,
#     edgecolor="black"
# )
# plt.title("Distribution of Asteroid Diameters")
# plt.xlabel("Maximum Diameter (KM)")
# plt.ylabel("Frequency")
# plt.tight_layout()
# plt.show()
#
#
# # 3. Top 10 Largest Asteroids
# top_10 = asteroid_clean.nlargest(
#     10, "Max_Diameter_KM"
# )
#
# plt.figure(figsize=(10, 6))
# plt.barh(
#     top_10["Asteroid_Name"],
#     top_10["Max_Diameter_KM"]
# )
# plt.title("Top 10 Largest Asteroids")
# plt.xlabel("Maximum Diameter (KM)")
# plt.ylabel("Asteroid Name")
# plt.gca().invert_yaxis()
# plt.tight_layout()
# plt.show()
#

# STEP 12: EXPORT DATASET TO CSV

# Export cleaned asteroid dataset
file_name = "NASA_Asteroid_Analysis.csv"

asteroid_clean.to_csv(
    file_name,
    index=False,
    encoding="utf-8"
)

# print("Dataset exported successfully!")
# print("File Name:", file_name)
# print("Total Records Exported:", len(asteroid_clean))


# STEP 13: VERIFY EXPORTED CSV

# Read exported CSV file
asteroid_check = pd.read_csv("NASA_Asteroid_Analysis.csv")

print("CSV Verification Successful!")

print("\nDataset Shape:")
print(asteroid_check.shape)

print("\nFirst 5 Records:")
print(asteroid_check.head())

print("\nColumn Names:")
print(asteroid_check.columns.tolist())




