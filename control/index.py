from run import app


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello World!'


