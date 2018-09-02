import pandas as pd
import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer


# Sanity check that python3
print ("Magic starts");

# Read data from JSON
with open("db-3.json") as datafile:
    data = json.load(datafile)
    d = pd.DataFrame(data)
    df = d.set_index("name", drop = False)

# Do pair-wise matching
nOfEntries = len(df.index)
last = nOfEntries - 1

c1 = []
c2 = []
pScore = []

for i in range(last):
    for j in range((i+1),(last+1)):
        firstCompany = df.iloc[i]
        secondCompany = df.iloc[j]
        c1.append(firstCompany["name"])
        c2.append(secondCompany["name"])
        #print(firstCompany["name"] + "\t\t" +
        #secondCompany["name"] + "\t\t" + str(random.randint(50,99)) +"%")

        vect = TfidfVectorizer(min_df=1)
        tfidf = vect.fit_transform([firstCompany["added"], secondCompany["added"]])
        res = (tfidf * tfidf.T).A
        print(res)

#print(c1)
