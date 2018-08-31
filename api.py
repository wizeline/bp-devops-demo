"""A simple python api"""
import os
from flask import Flask
from flask import jsonify

APP = Flask(__name__)

@APP.route("/")
def url_root():
    """just a health check"""
    return "OK"

@APP.route("/_health")
def url_health():
    """just a health check"""
    return "OK"


@APP.route("/message")
def url_cidr_to_mask():
    """returns the env var value"""
    res = {
        "message": os.environ.get("MESSAGE", "nothing"),
    }
    return jsonify(res)


if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=8000)
