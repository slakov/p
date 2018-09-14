from flask import Flask, jsonify
from flask import request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/api')
def get_mission():
    mission = request.args.get('mission')
    rmission = mission[::-1]

    return rmission

if __name__ == '__main__':
    app.run(debug=True)
