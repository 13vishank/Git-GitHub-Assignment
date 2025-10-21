from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Guyzz"

@app.route('/api')
def api():
    data = {"message": "Hello from the new and improved API!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)