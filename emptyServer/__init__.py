#!/usr/bin/python3
'''running via "fflask run -h localhost -p $PORT"'''
import json
import logging
from flask import Flask
from flask import request


def process1():
    '''First process in /api'''
    logging.info("run process1")


def process2(args):
    """Second process in /api
        with checking notawaiting argument"""
    message = ""
    if args.get("notawaiting"):
        if args.get("notawaiting") == "1":
            message += "ERROR::"
    message += "run process2"
    logging.info(message)


def process3():
    '''Third process in /api'''
    logging.info("run process3")


def create_app():
    '''Creating Flask server and routes'''
    app = Flask(__name__)
    logging.basicConfig(
        filename='log', format='%(asctime)-15s %(message)s', level=logging.INFO)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    @app.route('/')
    def index():
        '''/ route. Logging ERROR'''
        message = ""
        message += "ERROR::"

        message += "method="+request.method+" url="+request.url
        if request.args:
            message += " args="+json.dumps(request.args)
        else:
            message += " args=none"
        logging.info(message)

        return 'This one catches everything else'

    @app.route('/api')
    def api():
        '''/api route. General route'''
        message = ""
        if(request.method != "GET" or request.args.get("invalid") == "1"):
            message += "ERROR::"

        message += "method="+request.method+" url="+request.url
        if request.args:
            message += " args="+json.dumps(request.args)
        else:
            message += " args=none"
        logging.info(message)
        process1()
        process2(request.args)
        process3()
        return 'Hello, World API'

    @app.route('/<path:other>')
    def fallback():
        '''All routes except /api and /. Logging error'''
        message = ""
        message += "ERROR::"

        message += "method="+request.method+" url="+request.url
        if request.args:
            message += " args="+json.dumps(request.args)
        else:
            message += " args=none"
        logging.info(message)

        return 'This one catches everything else'
    return app
