import pandas as pd
import requests
server_address = "http://127.0.0.1:5000/"
playstoreData = pd.read_csv('../data/googleplaystore.csv')
single_row = playstoreData.sample()
row_kv_format = single_row.to_dict(orient='records')
r = requests.post(server_address + "ingestdata", json=row_kv_format)
print(r.status_code, r.reason)
