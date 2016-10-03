from bin import app
from flask import render_template, request


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    # return 'spec'
