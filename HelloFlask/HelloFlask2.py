from flask import Blueprint

hello_api = Blueprint('hello_api', __name__)


@hello_api.route('/hello')
def hello_world():
    return 'Hello World 2!'
