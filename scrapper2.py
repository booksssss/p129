import requests
from bs4 import BeautifulSoup
import pandas as pd

starturl = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(starturl)

soup = BeautifulSoup(page.text, "html.parser")

startTable = soup.find_all("table", {"class": "wikitable sortable"})
totalTable = len(startTable)
print(totalTable)

tempList = []
tableRows = startTable[1].find_all("tr")
for tr in tableRows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    tempList.append(row)

starName = []
distance = []
mass = []
radius = []

for i in range(1,len(tempList)):
    starName.append(tempList[i][0])
    distance.append(tempList[i][5])
    mass.append(tempList[i][7])
    radius.append(tempList[i][8])

headers = ["starName", "distance", "mass", "radius"]
df2 = pd.DataFrame(list(zip(starName, distance, mass, radius)),columns = ["starName", "distance", "mass", "radius"])
print(df2)
df2.to_csv("dwarfstars.csv", index = True, index_label="ie")

