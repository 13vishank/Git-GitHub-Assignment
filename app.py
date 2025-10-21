from flask import Flask, jsonify, request
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['todo_db']
collection = db['items']

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Guyzz"

@app.route('/api')
def api():
    data = {"message": "Hello from the new and improved API!"}
    return jsonify(data)

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    if item_name and item_description:
        collection.insert_one({"itemName": item_name, "itemDescription": item_description})
        return "Item saved successfully"
    return "Missing data", 400

if __name__ == '__main__':
    app.run(debug=True)