from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"


db = SQLAlchemy(model_class=Base)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    view_name = db.Column(db.String(128))
    package_name = db.Column(db.String(128))
    version = db.Column(db.String(128))
    hash = db.Column(db.String(256))
    id_file = db.Column(db.String(36))


# initialize the app with the extension
db.init_app(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World !</p>"