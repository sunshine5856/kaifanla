from flask import Flask
from control.index import *

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
