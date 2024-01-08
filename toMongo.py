from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
df = pd.read_csv('cleaned_data.csv')
data_dict = df.to_dict(orient='records')
uri = "mongodb+srv://hs414171:8639690@cluster0.9zubthz.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['JobPortal']
collection = db['JobInfo']

collection.insert_many(data_dict)
print(collection.count_documents({}))
