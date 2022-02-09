# Codeforces parser of top 10 with highest rating 

import requests, lxml, pprint
from bs4 import BeautifulSoup

response = requests.get(url="https://codeforces.com/")
soup = BeautifulSoup(response.text, "lxml")
data = soup.select("table tr td")[:30]
top10 = []

for i in range(0, 30, 3):
    profile = {"place": int(data[i].text), "username": data[i+1].text, "rating": int(data[i+2].text)}
    top10.append(profile)

pprint.pprint(top10)