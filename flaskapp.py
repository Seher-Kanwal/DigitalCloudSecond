import requests as requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Api!'


def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/nlptown/bert-base-multilingual-uncased-sentiment"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


@app.route('/Scoring/<string:x>')
def hell(x):
   return str(2)


if __name__ == '__main__':
    app.run()
