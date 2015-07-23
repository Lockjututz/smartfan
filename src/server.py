from flask import Flask, request, render_template
from os import environ
app = Flask(__name__)

@app.route("/")
def index():
    #TODO return template with graphs and charts
    return render_template('index.html')

@app.route("/storelogs/", methods=['POST'])
def storelogs():
    app.logger.debug("Storing data: %s end of data" % request.json['data'])
    return ""

def checkForCredentials():
    if environ['smartfandb_username'] == None or environ['smartfandb_password'] == None:
        raise EnvironmentError('Missing OS environment variables smartfandb_username and/or smartfandb_password')

if __name__ == "__main__":
    checkForCredentials()
    app.run(port=8071,debug=True)
#    app.run(port=8071)
