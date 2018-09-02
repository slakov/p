import pandas as pd
import json
import random


print ("Magic starts");

with open("db.json") as datafile:
    data = json.load(datafile)
    d = pd.DataFrame(data)
    df = d.set_index("name", drop = False)

nOfEntries = len(df.index)
last = nOfEntries - 1

for i in range(last):
    for j in range((i+1),(last+1)):
        firstCompany = df.iloc[i]
        secondCompany = df.iloc[j]
        print(firstCompany["name"] + "\t\t" +
        secondCompany["name"] + "\t\t" + str(random.randint(50,99)) +"%")
