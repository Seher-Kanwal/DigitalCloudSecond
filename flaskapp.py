import requests as requests
from flask import Flask
import fasttext


model = fasttext.load_model('fasttextmodel.bin')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Api!'


def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/nlptown/bert-base-multilingual-uncased-sentiment"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


@app.route('/Scoring1/<string:x>')
def predict(x):
  output = model.predict(x)
  label = output[0][0].split('__label__')[1]
  if label in ['4', '5']:
    result = str(2)
  elif label == '3':
    result = str(1)
  elif float(label) < 2:
    result = str(0)
  else :
    result = str(0)
  return  result



if __name__ == '__main__':
    app.run()
