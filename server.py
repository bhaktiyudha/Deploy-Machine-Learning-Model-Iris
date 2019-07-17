import pickle
import json
import numpy as np
from flask import Flask, request, jsonify

model = pickle.load(open('data/model.pkl','rb'))
app = Flask(__name__)

@app.route('/apiIris',methods=['POST'])
def getIris():
    array = request.get_json(force=True)
    prediction = model.predict([array['iris']])
    return json.dumps({"result":prediction[0]})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
