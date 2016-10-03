import sqlite3


class User(object):
    def __init__(self):
        # self.user = 'root'
        # self.password = 'password'
        # self.database = 'user'
        # self.host = '127.0.0.1'
        # self.port = 3306
        self.db = self.db_connect
        self.cursor = self.db.cursor()

    @property
    def db_connect(self):
        connect = sqlite3.connect('../data/user.db')
        print "Opened database successfully"
        return connect

    def add_user(self):
        if self.db:
            print 'exist'
            self.db.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
        else:
            print 'not exist'

# user = User()
# user.add_user()
