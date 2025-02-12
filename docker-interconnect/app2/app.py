import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/call-app1', methods=['GET'])
def call_app1():
    response = requests.get("http://app1:5000/api/message")  # Use service name `app1`
    return jsonify({"response_from_app1": response.json()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
