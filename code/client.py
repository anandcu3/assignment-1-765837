import pandas as pd
import requests
import time
import threading
import numpy as np


class DataPushThread(threading.Thread):
     def __init__(self, number_of_requests=5000):
         super(DataPushThread, self).__init__()
         self.number_of_requests = number_of_requests

     def run(self):
        prev_time = time.time()
        response_times = []
        for i in range(self.number_of_requests):
            single_row = playstoreData.sample()
            print("Sending data for app : ", ascii(single_row.loc[single_row.index[0],'App']))
            row_kv_format = single_row.to_dict(orient='records')
            row_kv_format[0]["id"] = int(single_row.index[0])
            start_time = time.time()
            r = requests.post(server_address + "ingestdata", json=row_kv_format)
            time_taken = time.time() - start_time
            response_times.append(time_taken)
            print("Received code : ",r.status_code, r.reason, "in ", time_taken,"seconds." )
            if r.status_code != 200:
                print("############################")
                print("REQUEST FAILED!!!", int(single_row.index[0]))
                print("############################")
        print("asdfghjkl",time.time()-prev_time)
        print(np.mean(response_times),np.max(response_times),np.min(response_times), np.std(response_times))



server_address = "http://35.228.81.87/"
playstoreData = pd.read_csv('../data/googleplaystore.csv')
number_of_concurrent_threads = 2
#print("Starting ",number_of_concurrent_threads, "threads")
prev_time = 0
for _ in range(number_of_concurrent_threads):
    thr = DataPushThread()
    thr.start()
    prev_time=time.time()
