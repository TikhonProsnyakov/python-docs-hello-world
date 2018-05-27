from flask import Flask
import pymongo
from bson.json_util import dumps
from testclass import TestClass


app = Flask(__name__)

mongo_uri = 'mongodb://developer:cosy@ds016098.mlab.com:16098/bot'
conn = pymongo.MongoClient(mongo_uri)
db = conn['bot']
user_collection = db["users"]

@app.route('/')
def hello_world():
  testclass = TestClass()
  return testclass.getString()

if __name__ == '__main__':
  app.run()
