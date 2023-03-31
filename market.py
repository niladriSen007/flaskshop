from flask import *
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"   
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# uri = Uniform Resource Identifier
db=SQLAlchemy(app)

app.app_context().push()

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length=20), nullable=False, unique=True)
    price = db.Column(db.Integer(),nullable=False)
    barcode = db.Column(db.String(length=12),nullable=False,unique=True,)
    description = db.Column(db.String(length=1024),nullable=False)

    def __repr__(self):
        return f"Item {self.name}"

@app.route("/")
def home():
    return (render_template("home.html"))

@app.route("/name/<username>")
def name(username):
    return (f"Hi {username} ")

@app.route("/amount/<age>")
def amount(age):
    return (f"Age = {age}")

@app.route("/market")
def market():
    items = [
        {
          "id":1,
          "name":"Phone",
          "barcode":"123",
          "price":500
        },
         {
          "id":2,
          "name":"Laptop",
          "barcode":"234",
          "price":600
        },
         {
          "id":3,
          "name":"Dresser",
          "barcode":"345",
          "price":700
        }
    ]
    return render_template("market.html",items = items)



if __name__ == "__main__":
    app.run(debug = True)