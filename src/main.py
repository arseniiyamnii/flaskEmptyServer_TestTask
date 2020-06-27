#!/usr/bin/python3

import os
from flask import Flask
from flask import request
import time
import logging
import json

def process1():
    logging.info("run process1")

def process2(args):
    message=""
    if args.get("notawaiting"):
        if args.get("notawaiting")=="1":
            message+="ERROR::"
    message+="run process2"
    logging.info(message)

def process3():
    logging.info("run process3")

app = Flask(__name__)
logging.basicConfig(filename='log',format='%(asctime)-15s %(message)s', level=logging.INFO)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
@app.route('/')
def index():
    message=""
    message+="ERROR::"
    #print(json.dumps(request.args))
    #logging.info(request.method,request.url,request.args,time.time)
    message+="method="+request.method+" url="+request.url
    if request.args:
        message+=" args="+json.dumps(request.args)
    else:
        message+=" args=none"
    logging.info(message)
    #print("method= ",request.method)
    #print("url= ",request.url)
    #print("args= ",request.args)
    #print("time= ", time.time())
    return('This one catches everything else')

@app.route('/api')
def api():
    message=""
    if(request.method!="GET" or request.args.get("invalid")=="1"):
        message+="ERROR::"
        #print(json.dumps(request.args))
        #logging.info(request.method,request.url,request.args,time.time)
    message+="method="+request.method+" url="+request.url
    if request.args:
        message+=" args="+json.dumps(request.args)
    else:
        message+=" args=none"
    logging.info(message)
    process1()
    process2(request.args)
    process3()
    return('Hello, World API')

@app.route('/<path:other>')
def fallback(other):
    message=""
    message+="ERROR::"
    #print(json.dumps(request.args))
    #logging.info(request.method,request.url,request.args,time.time)
    message+="method="+request.method+" url="+request.url
    if request.args:
        message+=" args="+json.dumps(request.args)
    else:
        message+=" args=none"
    logging.info(message)
    #print("method= ",request.method)
    #print("url= ",request.url)
    #print("args= ",request.args)
    #print("time= ", time.time())
    return 'This one catches everything else'

if __name__ == '__main__':
    app.run(host="localhost", port=os.environ.get('PORT'))

