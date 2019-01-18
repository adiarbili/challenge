import time
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Container World! '

@app.route('/sleep/', defaults={'seconds': 2 })
@app.route('/sleep/<int:seconds>')
def work(seconds):
    app.logger.info('Going to sleep for : {sec} seconds'.format(sec=seconds))
    time.sleep(seconds)
    app.logger.info('Slept for : {sec} seconds'.format(sec=seconds))
    return 'I was sleeping for {sec} seconds'.format(sec=seconds)

app.run(host='0.0.0.0', port=5000, debug=True)
