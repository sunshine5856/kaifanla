from run import app
from flask import render_template, request


@app.route('/manage/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


@app.route('/manage/login/verity', methods=['GET', 'POST'])
def verity():
    return 'Hello World!'


@app.route('/manage/index', methods=['GET', 'POST'])
def manage_index():
    return 'Hello World!'
