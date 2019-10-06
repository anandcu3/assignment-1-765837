from flask import Flask, request
import pymongo
import urllib

client = pymongo.MongoClient("mongodb://anandcu3:"+urllib.parse.quote("Rko@61999")+"@cluster0-shard-00-00-fbaws.gcp.mongodb.net:27017,cluster0-shard-00-01-fbaws.gcp.mongodb.net:27017,cluster0-shard-00-02-fbaws.gcp.mongodb.net:27017/admin?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["google_play_store"]
apps = db["app_information"]
app = Flask(__name__)


@app.route('/ingestdata', methods=['POST'])
def ingestData():
    x = apps.insert(request.json)
    print(x)
    return ""
