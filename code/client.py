import pandas as pd
import requests
import time
import threading

server_address = "http://127.0.0.1:5000/"
playstoreData = pd.read_csv('../data/googleplaystore.csv')
number_of_requests = 10000

for i in range(number_of_requests):
    single_row = playstoreData.sample()
    print("Sending data for app : ", ascii(single_row.loc[single_row.index[0],'App']))
    row_kv_format = single_row.to_dict(orient='records')
    row_kv_format[0]["id"] = int(single_row.index[0])
    start_time = time.time()
    r = requests.post(server_address + "ingestdata", json=row_kv_format)
    time_taken = time.time() - start_time
    print("Received code : ",r.status_code, r.reason, "in ", time_taken,"seconds." )
    if r.status_code != 200:
        print("############################")
        print("REQUEST FAILED!!!", int(single_row.index[0]))
        print("############################")
