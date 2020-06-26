#!/usr/bin/python3

import os
from flask import Flask
from flask import request
import time
import logging
import json

app = Flask(__name__)
logging.basicConfig(filename='log',format='%(asctime)-15s %(message)s', level=logging.INFO)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
@app.route('/')
def index():
    return("Hello World!")

@app.route('/api')
def api():
        return('Hello, World API')
@app.route('/<path:other>')
def fallback(other):
    message=""
    if(request.method!="GET" or request.args.get("invalid")=="1"):
        message+="ERROR::"
        #print(json.dumps(request.args))
        #logging.info(request.method,request.url,request.args,time.time)
    message+="methodSUKA="+request.method+" url="+request.url
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

