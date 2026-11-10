import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
books = soup.find_all('article', class_='product_pod')

data = []
#Extracting book information
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    #print(f'Title: {title}, Price: {price}, Availability: {availability}')
    data.append({
        'title': title,
        'price': price,
        'availability': availability
    })
df = pd.DataFrame(data)
book_price = pd.to_numeric( df["price"].str.replace("£", "",))
#print(df)
# print("Minimum:", book_price.min())
# print("Maximum:", book_price.max())
# print("Mean:", book_price.mean())
# print("Average:", book_price.mean())
# print("Range:", book_price.max() - book_price.min())
# print("Standard Deviation", book_price.std(ddof=0))

#print(f'Number of books found: {len(books)}')
#print(soup.prettify())
#print(soup.title.get_text())




# Step 1: Arsenal fixture URL
url = "https://www.premierleague.com/en/news/4675097/all-380-fixtures-for-202627-premier-league-season"

# Step 2: Request the webpage
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=30)
response.raise_for_status()

# Step 3: Parse the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract webpage text
text = soup.get_text("\n", strip=True)
lines = [line.strip() for line in text.splitlines() if line.strip()]

# Step 5: Find lines containing Arsenal
arsenal_lines = [
    line for line in lines
    if "arsenal" in line.lower()
]

print("Arsenal-related lines found:", len(arsenal_lines))

for line in arsenal_lines:
    print(line)

# Step 6: Save the extracted text to CSV
df = pd.DataFrame({"fixture_text": arsenal_lines})
df.to_csv("arsenal_fixtures.csv", index=False)

print("\nData saved to arsenal_fixtures.csv")
print(df.head(10))
# Number of extracted lines
print("Total Arsenal-related lines:", len(df))

# Check for duplicate lines
print("Duplicate lines:", df.duplicated().sum())

# Display all extracted lines
print(df.to_string(index=False))


import math

# Arsenal's recent league goals
arsenal_scored = [0, 2, 2, 0, 2]
arsenal_conceded = [1, 1, 0, 3, 1]

# Enter Nottingham Forest's actual recent league goals here
forest_scored = [1, 1, 2, 0, 1]
forest_conceded = [1, 2, 1, 1, 0]

# Average goals
arsenal_attack = sum(arsenal_scored) / len(arsenal_scored)
arsenal_defence = sum(arsenal_conceded) / len(arsenal_conceded)

forest_attack = sum(forest_scored) / len(forest_scored)
forest_defence = sum(forest_conceded) / len(forest_conceded)

# Simple expected-goals estimates
arsenal_xg = (arsenal_attack + forest_defence) / 2
forest_xg = (forest_attack + arsenal_defence) / 2

# Poisson probability of scoring a particular number of goals
def goal_probability(expected_goals, goals):
    return (
        math.exp(-expected_goals)
        * expected_goals**goals
        / math.factorial(goals)
    )

# Calculate scoreline probabilities
results = []

for arsenal_goals in range(6):
    for forest_goals in range(6):
        probability = (
            goal_probability(arsenal_xg, arsenal_goals)
            * goal_probability(forest_xg, forest_goals)
        )
        results.append(
            (arsenal_goals, forest_goals, probability)
        )

results.sort(key=lambda item: item[2], reverse=True)

print("Arsenal expected goals:", round(arsenal_xg, 2))
print("Forest expected goals:", round(forest_xg, 2))
print("\nMost likely scorelines:")

for arsenal_goals, forest_goals, probability in results[:5]:
    print(
        f"Arsenal {arsenal_goals} - {forest_goals} Forest: "
        f"{probability:.1%}"
    )

# Overall win/draw/loss probabilities
arsenal_win = sum(p for a, f, p in results if a > f)
draw = sum(p for a, f, p in results if a == f)
forest_win = sum(p for a, f, p in results if a < f)

total = arsenal_win + draw + forest_win

print("\nMatch outcome estimates:")
print(f"Arsenal win: {arsenal_win / total:.1%}")
print(f"Draw:        {draw / total:.1%}")
print(f"Forest win:  {forest_win / total:.1%}")






# url = "https://eto.ttp.com.ng/customer/showWallet"
#
# response = requests.get(url, timeout=30)
#
# #print("Status code:", response.status_code)
# #print("Final URL:", response.url)
#
# response.raise_for_status()
#
# soup = BeautifulSoup(response.text, "html.parser")
# #print(soup.prettify())
#
# #print("Page title:", soup.title.get_text(strip=True) if soup.title else "No title")
#
# # Check for HTML tables
# tables = soup.find_all("table")
# print("Number of tables found:", len(tables))
#
# for i, table in enumerate(tables):
#     print(f"\nTable {i + 1}:")
#     print(table.get_text(" ", strip=True)[:1000])
#
#
# # Load your authorized wallet export
# df = pd.read_csv("wallet_export.csv")
#
# # Convert balances to numeric values
# df["balance"] = pd.to_numeric(
#     df["balance"].astype(str).str.replace(",", "", regex=False),
#     errors="coerce"
# )
#
# # Analyze balances
# print("Number of wallet records:", len(df))
# print("Valid balances:", df["balance"].count())
# print("Total balance:", df["balance"].sum())
# print("Minimum balance:", df["balance"].min())
# print("Maximum balance:", df["balance"].max())
# print("Average balance:", df["balance"].mean())
# print("Balance range:", df["balance"].max() - df["balance"].min())
# print("Total Wallet Balance:", "total_balance")



