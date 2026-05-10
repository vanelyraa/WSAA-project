from flask import Flask, jsonify, request, abort, render_template, redirect
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__, static_url_path="", static_folder=".")

app.secret_key = "secret123"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login" 

cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

from trackerDAO import trackerDAO
from supplierDAO import supplierDAO

users = {"admin": {"password": "admin123"}}

class User(UserMixin):
    def __init__(self, username):
        self.id = username  

@login_manager.user_loader
def load_user(username):
    if username in users:
        return User(username)
    return None

@app.route('/')
@cross_origin()
@login_required
def index():
    return render_template("tracker.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            login_user(User(username))
            return redirect("/")
        else:
            return abort(401)

    else:
        return ('''
        <h2>Login</h2>
        <form action="" method="post">
            <p><input type="text" name="username" placeholder="Username">
            <p><input type="password" name="password" placeholder="Password">
            <p><input type="submit" value="Login">
        </form>''')

# GET all shipments
@app.route("/shipments")
@cross_origin()
@login_required
def getAll():
    results = trackerDAO.getAll()
    return jsonify(results)

# Find by ID
@app.route("/shipments/<int:id>")
@cross_origin()
@login_required
def findById(id):
    foundShipment = trackerDAO.findByID(id)
    return jsonify(foundShipment)

# Create
@app.route("/shipments", methods=["POST"])
@cross_origin()
@login_required
def create():
    if not request.json:
        abort(400)
    shipment = {
        "status": request.json["status"],
        "planned_eta": request.json["planned_eta"],        
        "actual_eta": request.json["actual_eta"],
        "item_code": request.json["item_code"],
        "supplier_id": request.json["supplier_id"]
    }
    addedShipment = trackerDAO.create(shipment)
    return jsonify(addedShipment)

# Update
@app.route("/shipments/<int:id>", methods=["PUT"])
@cross_origin()
@login_required
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
    if "supplier_id" in reqJson:
        foundShipment["supplier_id"] = reqJson["supplier_id"]    
    if "actual_eta" in reqJson:
        foundShipment["actual_eta"] = reqJson["actual_eta"]
    if "item_code" in reqJson:
        foundShipment["item_code"] = reqJson["item_code"]

    trackerDAO.update(id, foundShipment)
    return jsonify(foundShipment)

# Delete
@app.route("/shipments/<int:id>", methods=["DELETE"])
@cross_origin()
@login_required
def delete(id):
    trackerDAO.delete(id)
    return jsonify({"done": True})

# Supplier routes
# GET all suppliers
@app.route("/suppliers")
@cross_origin()
@login_required
def getAllSuppliers():
    results = supplierDAO.getAll()
    return jsonify(results)

# Create supplier
@app.route("/suppliers", methods=["POST"])
@cross_origin()
@login_required
def createSupplier():
    if not request.json:
        abort(400)
    supplier = {
        "supplier_name": request.json["supplier_name"],
        "country": request.json["country"]
    }
    addedSupplier = supplierDAO.create(supplier)
    return jsonify(addedSupplier)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")

# Run application
if __name__ == "__main__":
    app.run(debug = True)


# Render template: https://stackoverflow.com/questions/63333562/best-practice-of-flask-route-for-app-route-index-or-index-html
# User authentication: https://www.geeksforgeeks.org/python/flask-login-without-database-python/ delete?
# User authentication: https://stackoverflow.com/questions/66738115/simple-flask-login-example-is-this-the-correct-way
# User authentication: https://nrodrig1.medium.com/flask-login-no-flask-sqlalchemy-d62310bb43e3
# User authentication: https://stackoverflow.com/questions/65590876/flask-login-without-database
# User authentication: https://stackoverflow.com/questions/66738115/simple-flask-login-example-is-this-the-correct-way
# Logout: https://stackoverflow.com/questions/47670382/how-to-logout-a-user-from-the-database-with-flask-login