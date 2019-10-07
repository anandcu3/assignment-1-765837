import pymongo
import pandas as pd
import threading

client = pymongo.MongoClient("mongodb://anandcu3:h3GuvlswXSUsRgCb@cluster0-shard-00-00-fbaws.gcp.mongodb.net:27017,cluster0-shard-00-01-fbaws.gcp.mongodb.net:27017,cluster0-shard-00-02-fbaws.gcp.mongodb.net:27017/admin?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["google_play_store"]
apps = db["app_information"]
playstoreData = pd.read_csv('../data/googleplaystore.csv')
playstoreData['Id'] = playstoreData.index

class checkConcurrentRequests(threading.Thread):
        def __init__(self):
            super(checkConcurrentRequests, self).__init__()

        def run(self):
            for i in range(1000):
                single_row = playstoreData.sample()
                row_to_ingest_json = single_row.to_dict(orient='records')
                apps.insert(row_to_ingest_json)

for i in range(6):
    checkConcurrentRequests().start()
