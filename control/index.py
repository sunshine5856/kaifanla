from bin import app
from flask import render_template, request
from model.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@app.route('/', methods = ['GET', 'POST'])
def index():
    DB_CONNECT_STRING = 'sqlite:///../data/user.db'
    engine = create_engine(DB_CONNECT_STRING, echo = True)
    dbsession = sessionmaker(bind = engine)
    print dbsession
    user = User(name = 'jft', password = 'jft')
    dbsession.add(user)
    dbsession.commit()
    query = dbsession.query(User)
    # return render_template('index.html')
    return query.all()
    # return 'spec'
