from datetime import datetime

import joblib
import pandas as pd
import pytz
from flask import Flask
from flask import request
from flask_cors import CORS
from termcolor import colored


back_end_api = Flask(__name__)
CORS(back_end_api)


@app.route('/')
def index():
    return 'OK'




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
