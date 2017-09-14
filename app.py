from flask import Flask
from flask import render_template, request
import requests
import cPickle as pickle
from model import MyModel, get_data
import pandas as pd
from utils import preprocess_series
import json
import time

app = Flask(__name__)





@app.route('/',methods=['GET','POST'])
# name = request.args.get('name')
def hello():
    return render_template('hello.html')

@app.route('/model_predict',methods=['POST'])
def model_predict():
    with open('model.pkl') as f:
        model = pickle.load(f)
    url = 'http://galvanize-case-study-on-fraud.herokuapp.com/data_point'
    ct = 10
    stored_id = set()
    preds = []
    start = time.time()
    while True and ct > 0:
        data = requests.get(url).json()
        ob_id = data['object_id']
        if ob_id not in stored_id:
            d = pd.Series(data)
            X = preprocess_series(d)
            preds.append(round(model.predict_proba(X)[0][1],2))
            stored_id.add(ob_id)
        ct -= 1
    process_time = time.time() - start
    for i in xrange(10):
        return render_template('output.html',preds=preds,process= process_time)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
