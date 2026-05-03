from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from flask import render_template

app = Flask(__name__, static_url_path="", static_folder=".")
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

from trackerDAO import trackerDAO

@app.route('/')
@cross_origin()
def index():
    return render_template("tracker.html")

# GET all shipments
@app.route("/shipments")
@cross_origin()
def getAll():
    results = trackerDAO.getAll()
    return jsonify(results)

# Find by ID
@app.route("/shipments/<int:id>")
@cross_origin()
def findById(id):
    foundShipment = trackerDAO.findByID(id)
    return jsonify(foundShipment)

# Create
@app.route("/shipments", methods=["POST"])
@cross_origin()

def create():
    if not request.json:
        abort(400)
    shipment = {
        "status": request.json["status"],
        "planned_eta": request.json["planned_eta"],
        "supplier_code": request.json["supplier_code"],
        "supplier_name": request.json["supplier_name"],
        "actual_eta": request.json["actual_eta"],
        "item_code": request.json["item_code"]
    }
    addedShipment = trackerDAO.create(shipment)
    return jsonify(addedShipment)

# Update
@app.route("/shipments/<int:id>", methods=["PUT"])
@cross_origin()
def update(id):
    foundShipment = trackerDAO.findByID(id)
    if not foundShipment:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json

    if "status" in reqJson:
        foundShipment["status"] = reqJson["status"]
    if "planned_eta" in reqJson:
        foundShipment["planned_eta"] = reqJson["planned_eta"]
    if "supplier_code" in reqJson:
        foundShipment["supplier_code"] = reqJson["supplier_code"]
    if "supplier_name" in reqJson:
        foundShipment["supplier_name"] = reqJson["supplier_name"]
    if "actual_eta" in reqJson:
        foundShipment["actual_eta"] = reqJson["actual_eta"]
    if "item_code" in reqJson:
        foundShipment["item_code"] = reqJson["item_code"]

    trackerDAO.update(id, foundShipment)
    return jsonify(foundShipment)

# Delete
@app.route("/shipments/<int:id>", methods=["DELETE"])
@cross_origin()
def delete(id):
    trackerDAO.delete(id)
    return jsonify({"done": True})

# Run application
if __name__ == "__main__":
    app.run(debug = True)


# Render template: https://stackoverflow.com/questions/63333562/best-practice-of-flask-route-for-app-route-index-or-index-html