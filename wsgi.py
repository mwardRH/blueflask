import socket
from flask import Flask, request

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello BLUE!"

@app.route("/hostname/")
def return_hostname():
    return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)

if __name__ == "__main__":
    application.run()
