from flask import Flask,render_template,request,jsonify
#from source import inpo,clear
import subprocess
import os, sys
from subprocess import check_output
import time
import json
from flask import request, redirect
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import matplotlib.pyplot as plt
#import seaborn as sns # for plot visualization
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('display.html')

@app.route('/background_process', methods=['GET', 'POST'])
def background_process():
        if request.method =="POST":
            calender = request.form['calender']
            return(calender)
        else:
                print("not available")

        subprocess.call(['python.exe','TempPrediction.py',])




@app.route('/indbig')
def indbig():
    return render_template('weather.html')


@app.route('/convertor')
def convertor():
    return render_template('display.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=True)
