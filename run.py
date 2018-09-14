from flask import Flask, render_template, jsonify, Blueprint
from random import *
from flask_cors import CORS
import requests

app = Flask(__name__,
            #static_folder = "./frontend/dist/js",
            template_folder = "./frontend/dist")

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18080)
