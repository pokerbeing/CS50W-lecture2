from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return '<h1 style="color:blue;">Hello, {}!</h1>'.format(name)
