from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase
import yaml
import hashlib
import os

def compute_hash(path):
    sha256_hash = hashlib.sha256()
    with open(path,"rb") as f:
    # Read and update hash string value in blocks of 4K
      for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

class Base(DeclarativeBase):
  pass

config = yaml.safe_load(open('./config.yaml').read())

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = config["database"]["type"] + ":///" + config["database"]["uri"] #"sqlite:///project.db"


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

@app.route("/download/<file_package>")
def download(file_package):
    module = Module.query.filter_by(package_name=file_package).first()
    if module == None:
        return 'module not found', 404
    module_path = os.path.join(config["volume"]["path"], module.id_file + ".js")
    module_hash = compute_hash(module_path)
    if module_hash != module.hash:
       return 'bad hash', 500
    return open(module_path).read()