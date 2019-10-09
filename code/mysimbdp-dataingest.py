import pymongo
import pandas as pd
import threading
import time
import numpy as np
client = pymongo.MongoClient("mongodb://anandcu3:h3GuvlswXSUsRgCb@cluster0-shard-00-00-fbaws.gcp.mongodb.net:27017,cluster0-shard-00-01-fbaws.gcp.mongodb.net:27017,cluster0-shard-00-02-fbaws.gcp.mongodb.net:27017/admin?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
print(client.test)
db = client["google_play_store"]
apps = db["app_information"]
playstoreData = pd.read_csv('../data/googleplaystore.csv')
playstoreData['Id'] = playstoreData.index

class checkConcurrentRequests(threading.Thread):
        def __init__(self):
            super(checkConcurrentRequests, self).__init__()

        def run(self):
            response_times = []
            prev_time = time.time()
            for i in range(100):
                single_row = playstoreData.sample()
                row_to_ingest_json = single_row.to_dict(orient='records')
                start_time = time.time()
                apps.insert(row_to_ingest_json)
                time_taken = time.time() - start_time
                print("Received code in ", time_taken,"seconds.")
                response_times.append(time_taken)
            print("Time taken for execution of the thread: ",time.time()-prev_time)
            print(np.mean(response_times),np.max(response_times),np.min(response_times), np.std(response_times))

for i in range(50):
    checkConcurrentRequests().start()
