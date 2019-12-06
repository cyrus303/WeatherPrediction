from flask import Flask,render_template,request,jsonify
#from source import inpo,clear
import subprocess
import os, sys
from subprocess import check_output
import time
import json
from flask import request, redirect

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('display.html')

@app.route('/background_process', methods=['GET', 'POST'])
def background_process():
        if request.method =="POST":
            calender = request.form['calender']
            #flash(calender)
            #process = subprocess.Popen(['python' , 'print.py' ],
            subprocess.call(['python','print.py',],stdout=open('output.txt','r+'))
#            out, err = process.communicate()
#            print(out)
        else:
            print("not available")


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
