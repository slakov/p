import pandas as pd
import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Sanity check that python3
print ("Magic starts");

# Read data from JSON
with open("dbtest.json") as datafile:
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
        # tfidf = vect.fit_transform([firstCompany["added"], secondCompany["added"],
        # firstCompany["needed"], secondCompany["needed"], firstCompany["mission"],
        # secondCompany["mission"]])

        tfidf = vect.fit_transform([firstCompany["added"], secondCompany["added"],
        firstCompany["needed"], secondCompany["needed"]])

        res = (tfidf * tfidf.T).A
        resFlat = res.ravel()

        # We dont need ones
        for index, value in enumerate(resFlat):
            if np.round(value) == 1:
                resFlat[index] = 0.0

        # Add pScore
        thisScore = np.round(max(resFlat)*100)
        pScore.append(thisScore)


outputTable = pd.DataFrame({"cmp1": c1, "cmp2": c2, "pScore": pScore})
outputTable.to_csv("out.csv")
#print(c1)
