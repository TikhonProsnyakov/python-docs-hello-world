from flask import Flask
import pymongo
from bson.json_util import dumps


app = Flask(__name__)

mongo_uri = 'mongodb://developer:cosy@ds016098.mlab.com:16098/bot'
conn = pymongo.MongoClient(mongo_uri)
db = conn['bot']
user_collection = db["users"]

@app.route('/')
def hello_world():
  user = user_collection.find({'id': 2})
  if user.count() > 0:
    return dumps(user.__getitem__(0))
  return "{}", 200

if __name__ == '__main__':
  app.run()
