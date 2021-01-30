
from flask import Flask


Application = Flask(__name__)


@Application.route("/")
def index():
    return 'Hello, Flask!'

