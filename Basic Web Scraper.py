import requests
from bs4 import BeautifulSoup

url = "https://weblandscape.co.uk/"   # Demo website

# Step 1: Website request
response = requests.get(url)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract data
quotes = soup.find_all("span", class_="text")

for q in quotes:
    print(q.text)
