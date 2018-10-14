from flask import Flask, render_template, Blueprint, request
from flask_cors import CORS
import requests
import json

from app.mecabpos import mecabpos
from app.mecabspace import mecabspace

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

@app.route('/api/kill', methods=['POST'])
def kill():
    last_ms = LAST_REQUEST_MS
    def shutdown():
        if LAST_REQUEST_MS <= last_ms:  # subsequent requests abort shutdown
            func = request.environ.get('werkzeug.server.shutdown')
            if func is None:
                raise RuntimeError('Not running with the Werkzeug Server')
            func()
        else:
            pass

    Timer(1.0, shutdown).start()  # wait 1 second
    return "Shutdown vue-mecab!"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18080)
