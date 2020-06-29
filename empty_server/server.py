#!/usr/bin/python3
'''running via "flask run -h localhost -p $PORT"'''
import json
import logging
from flask import Flask
from flask import request

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT',
                'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']


def process1():
    '''First process in /api'''
    error = "     "
    logging.info("%s :: run process1", error)


def process2(args):
    """Second process in /api
        with checking notawaiting argument"""
    error = "     "
    if args.get("notawaiting"):
        if args.get("notawaiting") == "1":
            error = "ERROR"
    logging.info("%s :: run process2", error)


def process3():
    '''Third process in /api'''
    error = "     "
    logging.info("%s :: run process3", error)


def create_app():
    '''Creating Flask server and routes'''
    app = Flask(__name__)
    logging.basicConfig(
        filename='log.log', format='%(asctime)-15s %(message)s', level=logging.INFO)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    @app.route('/', methods=HTTP_METHODS)
    def index():
        '''/ route. Logging ERROR'''
        error = "ERROR"
        if request.args:
            args = json.dumps(request.args)
        else:
            args = "none"
        logging.info('%s :: method=%s :: url=%s :: args=%s',
                     error, request.method, request.url, args)

        return 'This one catches everything else'

    @app.route('/api', methods=HTTP_METHODS)
    def api():
        '''/api route. General route'''
        error = "     "
        if(request.method != "GET" or request.args.get("invalid") == "1"):
            error = "ERROR"
        if request.args:
            args = json.dumps(request.args)
        else:
            args = "none"
        logging.info('%s :: method=%s :: url=%s :: args=%s',
                     error, request.method, request.url, args)
        process1()
        process2(request.args)
        process3()

        return 'Hello, World API'

    @app.route('/<path:other>', methods=HTTP_METHODS)
    def fallback(other):
        '''All routes except /api and /. Logging error'''
        error = "ERROR"
        if request.args:
            args = json.dumps(request.args)
        else:
            args = "none"
        logging.info('%s :: method=%s :: url=%s :: args=%s',
                     error, request.method, request.url, args)
        return 'This one catches everything else'
    return app
