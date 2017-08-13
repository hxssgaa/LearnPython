from flask import Blueprint

hello_api2 = Blueprint('hello_api_2', __name__)


@hello_api2.route('/hello2')
def hello_world():
    return 'Hello World 3!'
