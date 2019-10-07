import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb://anandcu3:h3GuvlswXSUsRgCb@cluster0-shard-00-00-fbaws.gcp.mongodb.net:27017,cluster0-shard-00-01-fbaws.gcp.mongodb.net:27017,cluster0-shard-00-02-fbaws.gcp.mongodb.net:27017/admin?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["google_play_store"]
apps = db["app_information"]
playstoreData = pd.read_csv('../data/googleplaystore.csv')
playstoreData['Id'] = playstoreData.index
row_to_ingest_json = playstoreData.to_dict(orient='records')
apps.insert(row_to_ingest_json)
