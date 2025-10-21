from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Guyzz"

@app.route('/api')
def api():
    data = {"message": "This is the API response"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)