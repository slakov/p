from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Read data from JSON
with open("db.json") as datafile:
    data = json.load(datafile)
    d = pd.DataFrame(data)
    df = d.set_index("name", drop = False)

    app = Flask(__name__)
    CORS(app)


    @app.route('/api')
    def get_mission():
        mission = request.args.get('mission')

        # Search for best partner
        nOfEntries = len(df.index)
        last = nOfEntries - 1

        bestParner = ""
        pScore = 0

        for i in range(last+1):

            currentCompany = df.iloc[i]
            currentCompanyName = currentCompany["name"]

            # Compute text similarity of mission and expertize
            vect = TfidfVectorizer(min_df=1)

            tfidf = vect.fit_transform([currentCompany["added"], mission])

            res = (tfidf * tfidf.T).A
            resFlat = res.ravel()

            # We dont need ones
            for index, value in enumerate(resFlat):
                if np.round(value) == 1:
                    resFlat[index] = 0.0

            # Compare pScore
            thisScore = np.round(max(resFlat)*100)
            if (thisScore > pScore):
                bestPartner = currentCompanyName
                pScore = thisScore

        return bestPartner


    if __name__ == '__main__':
        app.run(debug=True)
