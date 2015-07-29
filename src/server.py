from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from flask import Flask, request, render_template
import sensor_repository as repo
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    #TODO return template with graphs and charts
    return render_template('index.html')

@app.route("/storelogs/", methods=['POST'])
def storeLogs():
    app.logger.debug("Storing data: %s end of data" % request.json)
    repo.storeLogs(request.json)
    return ""

@app.route("/getlogs/", methods=['GET'])
def getLogsInInterval():
    fromDate = request.args.get('fromDate', '')
    toDate = request.args.get('toDate', '')
    logs = repo.getLogsBetween(fromDate, toDate)
    return logs

@app.route("/latestlog/", methods=['GET'])
def getLatestLog():
    return json.dumps(repo.getLatestLog())

def checkForCredentials():
    from os import environ
    try:
        if (environ['smartfandb_username'] is None or len(environ['smartfandb_username']) <= 0) \
        or (environ['smartfandb_password'] is None or len(environ['smartfandb_password']) <= 0):
            raise EnvironmentError('Missing OS environment variables smartfandb_username and/or smartfandb_password')
    except KeyError:
        raise EnvironmentError('Missing OS environment variables smartfandb_username and/or smartfandb_password')

if __name__ == "__main__":
    checkForCredentials()
    # debug options
#    app.run(port=8071,debug=True)
#    app.run(port=8071)
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(8071)
    IOLoop.instance().start()
    app.logger.info("Server running")
