import requests
from bs4 import BeautifulSoup

url = "https://www.premierleague.com/en/stats/top/players/goals"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

#Scraping the top goal scorers
statTable = soup.find("dvi", class_="stats-table")
scoreTable = statTable(0).find_all("tr")
for row in scoreTable:
    player = row.find("td", class_="stat-table__name").get_text(strip=True) if row.find("td", class_="stat-table__name") else None
    goals = row.find("td", class_="stat-table__name").get_text(strip=True)
    #print(f"{player}: {goals} goals")


print(soup.prettify())
