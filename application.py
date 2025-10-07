from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

#import ridge regresso and standard scaler pickle files.
ridge_model = pickle.load(open('models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)