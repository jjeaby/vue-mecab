from flask import Flask, render_template, Blueprint, request
from flask_cors import CORS
import requests
import json
import time
from threading import Timer
import os, inspect

from app.mecabpos import mecabpos
from app.mecabspace import mecabspace
from app.mecabmultinoun import mecabextractmultinoun

app = Flask(__name__,
            # static_folder = "./frontend/dist/js",
            template_folder="./frontend/dist")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

css = Blueprint('css', __name__, static_url_path='/css', static_folder='./frontend/dist/css')
js = Blueprint('js', __name__, static_url_path='/js', static_folder='./frontend/dist/js')

app.register_blueprint(css)
app.register_blueprint(js)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

@app.before_first_request
def update_last_request_ms():
    global LAST_REQUEST_MS
    LAST_REQUEST_MS = time.time() * 1000

@app.route('/api/mecabpos', methods=['POST'])
def mecab_pos():
    query = request.get_json()
    ret_pos = mecabpos(query["srcText"])
    return str(json.dumps(ret_pos, ensure_ascii=False));

@app.route('/api/mecabspace', methods=['POST'])
def mecab_space():
    query = request.get_json()
    ret_pos = mecabspace(query["srcText"])
    return str(json.dumps(ret_pos, ensure_ascii=False));

@app.route('/api/mecabmultinoun', methods=['POST'])
def mecab_extract_multi_nonw():
    query = request.get_json()
    ret_pos = mecabextractmultinoun(query["srcText"])
    return str(json.dumps(ret_pos, ensure_ascii=False));


@app.route('/api/kill', methods=['POST'])
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Shutdown vue-mecab!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=38080)
