import math
from flask import Flask
from HelloFlask2 import hello_api
from HelloFlask3 import hello_api2

app = Flask(__name__)
app.register_blueprint(hello_api)
app.register_blueprint(hello_api2)


@app.route('/')
def hello_world():
    return str(math.pi)


if __name__ == '__main__':
    app.run(debug=True)
