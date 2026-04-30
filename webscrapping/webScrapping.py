import csv

import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

print(response.status_code)
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

# search by tag
titles = soup.find_all("h3")
print(titles)

# search by class
countries = soup.find_all("div", class_="country")
print(countries)

# extact links
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

# save scraped data to a file

with open("links.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Titles","Links"])
    
    for link in links:
        writer.writerow([link.text.strip(), link.get("href")])