
from pymongo.mongo_client import MongoClient
from pymongo import MongoClient


uri = "mongodb://umadevip:mongodb@mongodb.c8kjfqfhvmko.us-west-2.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&retryWrites=false"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)