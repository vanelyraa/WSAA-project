from flask import Flask, jsonify
from trackerDAO import trackerDAO

app = Flask(__name__)

@app.route('/')
def index():
    return "Server working"

# GET all shipments
@app.route('/shipments')
def getAll():
    results = trackerDAO.getAll()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug = True)
