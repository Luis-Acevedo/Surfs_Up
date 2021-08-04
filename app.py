from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/Stats')
def stats():
    return 'Where stats will go'
# Make sure to run 'export FLASK_APP=app.py' and 'flask run' in terminal