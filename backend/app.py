from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/cdg"
mongo = PyMongo(app)
@app.route('/')
def index():
    return 'Welcome to Mentella'

@app.route('/allresources', methods=['GET'])
def allresources():
    value = request.args.get('value')
    print(value)
    online_users = mongo.db.clinics.find({"Speciality": value})
    myjson = []
    for i in online_users:
        del i['_id']
        myjson.append(i)
    return jsonify(myjson)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
