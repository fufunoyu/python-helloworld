from flask import Flask
from flask import json
import logging

tracebackDebug = 1

def logTraceBack():
    if(tracebackDebug == 1):
        logging.info(traceback.format_exc())

FORMAT = '%(asctime)s|%(levelname)s|%(message)s'
logging.basicConfig(filename="scannedFiles.log", filemode='w', level=logging.INFO, format=FORMAT)

app = Flask(__name__)

@app.route('/status')
def status():
    status_code = app.response_class(
        response = json.dumps({"result":"OK - healthy"}),status=200,mimetype='application/json'
    )
    app.logger.info('Status request successful!')
    return status_code

@app.route('/metrics')
def metrics():
    data = app.response_class(
        response = json.dumps({"data":{"UserCount": 140, "UserCountActive": 23}}),
        status = 200,
        mimetype = 'application/json'
    )
    app.logger.info('Metrics request successful!')
    return data

@app.route("/")
def hello():
    app.logger.info('Main request successful!')
    return "Hello World!"

if __name__ == "__main__":

    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    app.run(host='0.0.0.0')
