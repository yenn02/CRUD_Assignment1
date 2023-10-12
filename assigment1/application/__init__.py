from flask import Flask, session
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "8c41058000a090f3eec7183a670e87f963c13bcb"

import pymongo

conn = "mongodb+srv://yenj214:Yenjohn1314.@assignment1.rcceahx.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(conn, serverSelectionTimeoutMS=5000)
db = client.db

from application import routes
