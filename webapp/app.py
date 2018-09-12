from flask import Flask, jsonify
from flask import request


app = Flask(__name__)


@app.route('/api')
def get_mission():
    mission = request.args.get('mission')
    rmission = mission[::-1]

    return rmission

if __name__ == '__main__':
    app.run(debug=True)
