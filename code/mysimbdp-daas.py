from flask import Flask, request
from flask_restplus import Resource, Api
import pymongo
import jsons

client = pymongo.MongoClient("mongodb://anandcu3:h3GuvlswXSUsRgCb@cluster0-shard-00-00-fbaws.gcp.mongodb.net:27017,cluster0-shard-00-01-fbaws.gcp.mongodb.net:27017,cluster0-shard-00-02-fbaws.gcp.mongodb.net:27017/admin?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["google_play_store"]
apps_table = db["app_information"]
reviews_table = db["app_reviews"]
flaskApp = Flask(__name__)
app = Api(app = flaskApp)
app_information = app.namespace('appinfo', description='APIs concerning information about the applications from the play store')
app_reviews = app.namespace('appreviews', description='APIs concerning the reviews about the applications')

@app_information.route('/ingestdata')
class ingestData(Resource):
    def post(self):
        x = apps_table.insert(request.json)
        return ""

@app_information.route('/name/<name>')
class findAppbyName(Resource):
    def get(self, name):
        apps_table.create_index([('App', 'text')])
        response = list(apps_table.find({"$text": {"$search": name}}))
        return jsons.dumps(response)
    def post(self, name):
        apps_table.create_index([('App', 'text')])
        response = list(apps_table.find({"$text": {"$search": name}}))
        return jsons.dumps(response)

@app_reviews.route('/ingestdata')
class ingestData(Resource):
    def post(self):
        x = reviews_table.insert(request.json)
        return ""

@app_reviews.route('/name/<name>')
class findAppbyName(Resource):
    def get(self, name):
        apps_table.create_index([('App', 'text')])
        response = list(apps_table.find({"$text": {"$search": name}}))
        return jsons.dumps(response)
    def post(self, name):
        apps_table.create_index([('App', 'text')])
        response = list(apps_table.find({"$text": {"$search": name}}))
        return jsons.dumps(response)

flaskApp.run(host="0.0.0.0", port=80)
