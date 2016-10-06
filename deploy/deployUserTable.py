import sqlite3

conn = sqlite3.connect('../data/user.db')
print "Opened database successfully"

conn.execute('''CREATE TABLE user (
  id         INT,
  name       VARCHAR(255),
  age        VARCHAR(255),
  department VARCHAR(255),
  series     VARCHAR(255),
  password   VARCHAR(255),
  address    VARCHAR(255)
);''')
print "Table created successfully"

conn.close()
