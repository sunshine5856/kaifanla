from run import app
# from model import user
from flask import make_response, session, request


# show_user_profile
@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    # show the user profile for that user
    # show the user profile for that user
    # show the user profile for that user
    # show the user profile for that user
    # show the user profile for that user
    # show the user profile for that user
    return 'User %s' % username
    # resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
