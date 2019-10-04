from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/ingestdata', methods=['POST'])
def hello():
    print(request.json)
    return ""
