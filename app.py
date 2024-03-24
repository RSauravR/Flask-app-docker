from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, welcome to my first flask app. This is containerised by docker'

@app.route('/health')
def health():
    return 'Server is up and running'
