from flask import Flask
import pymongo
import pandas as pd
client = pymongo.MongoClient("mongodb://webUser:xxx123xxx@cluster0-shard-00-00.algwo.mongodb.net:27017,cluster0-shard-00-01.algwo.mongodb.net:27017,cluster0-shard-00-02.algwo.mongodb.net:27017/?ssl=true&replicaSet=atlas-am4cb3-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.sample_supplies # nome del database
result = pd.DataFrame(list(db.vendite.find()))
result = result.head(10)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return (result.to_html())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)