import socket
from flask import Flask, request

application = Flask(__name__)

@application.route("/")
def return_hostname():
    return "This is {} on {} running the BLUE version of the application \n".format(socket.gethostname(), request.remote_addr)

if __name__ == "__main__":
    application.run()
