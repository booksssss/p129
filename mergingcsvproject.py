from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_csv("dwarfstars.csv")
print(df.head())

print(df.shape)
df.info()
df["radius"] = df["radius"]*int((0.102763))
df["mass"] = df["mass"]*int((0.000954588))
df.to_csv("convertedStars.csv" )

