from flask import Flask, render_template
from threading import Thread
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/status')
def run():
    app.run(host="0.0.0.0", port=8080)

def main():
    server = Thread(target=run)
    server.start()