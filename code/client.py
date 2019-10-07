import pandas as pd
import requests
import time
import threading
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--number_of_concurrent_threads", help="Number of concurrent threads to push to the DAAS platform. Default is 6.",
                    type=int, default=6 )
parser.add_argument("-r", "--total_number_requests", help="Total number of data points to be pushed via the daas. Default is 10000. Will be dividied among all threads",
                    type=int, default=10000 )
parser.add_argument("--all", help="Use this argument to just push all the rows of the csv file through DAAS without random sampling.",
                    action="store_true", default=False )
parser.add_argument("--reviews", help="Use this argument to push data from the reviews file instead of the zpp information file.",
                    action="store_true", default=False)
args = parser.parse_args()

push_the_CSV = args.all
reviewData = args.reviews
number_of_concurrent_threads = args.number_of_concurrent_threads
number_of_requests = args.total_number_requests//number_of_concurrent_threads

server_address = "http://127.0.0.1:5000/"

def sendRequest(row_kv_format, server_address):
    start_time = time.time()
    if reviewData:
        server_address = server_address + "appreviews/"
    else:
        server_address = server_address + "appinfo/"
    r = requests.post(server_address + "ingestdata", json=row_kv_format)
    time_taken = time.time() - start_time
    print("Received code : ",r.status_code, r.reason, "in ", time_taken,"seconds." )
    if r.status_code != 200:
        print("############################")
        print("REQUEST FAILED!!!")
        print("############################")
    return time_taken


class DataPushThread(threading.Thread):
     def __init__(self, number_of_requests):
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
            time_taken = sendRequest(row_kv_format, server_address)
            response_times.append(time_taken)
        print("Time taken for execution of the thread: ",time.time()-prev_time)
        print(np.mean(response_times),np.max(response_times),np.min(response_times), np.std(response_times))


if reviewData:
    playstoreData = pd.read_csv('../data/googleplaystore_user_reviews.csv')
else:
    playstoreData = pd.read_csv('../data/googleplaystore.csv')

if push_the_CSV:
    playstoreData['Id'] = playstoreData.index
    for i in playstoreData.index:
        single_row = playstoreData.iloc[[i]]
        row_to_ingest_json = single_row.to_dict(orient='records')
        time_taken = sendRequest(row_to_ingest_json, server_address)
else:
    for _ in range(number_of_concurrent_threads):
        thr = DataPushThread(number_of_requests)
        thr.start()
