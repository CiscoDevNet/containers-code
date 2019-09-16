#!/usr/bin/env python

from flask import Flask,request
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return os.environ['HOSTNAME']

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
