from pymongo import MongoClient
client = MongoClient('mongodb+srv://sarudb:TGxiJW4Tajd7yRg8@pythondbcluster.srgz3py.mongodb.net/?retryWrites=true&w=majority&appName=pythondbcluster')
db = client['mydb']
users_collection = db['users']

