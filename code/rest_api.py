from flask import Flask, request
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client["google_play_store"]
apps = db["app_information"]
app = Flask(__name__)


@app.route('/ingestdata', methods=['POST'])
def hello():
    x = apps.insert(request.json)
    print(x)
    return ""
